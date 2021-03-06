from flask import Flask, redirect, request, session, render_template, flash
from mysqlconnections import MySQLConnector
import md5
import os, binascii
import re
from flask_bcrypt import Bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app=Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "Meh"
mysql = MySQLConnector(app,"the_wall_db")
@app.route('/')
def index():
    if 'logged' in session:
        print session['logged'][0]['first_name']
        return redirect('/wall')
    else:
        return render_template('index.html')
@app.route('/wall', methods= ['get'])
def wall():
    messages = "SELECT `users`.`first_name`, `messages`.`id`, `messages`.`created_at`, `messages`.`message` from the_wall_db.users JOIN messages ON users.id = messages.user_id ORDER BY messages.id"
    session['print'] = mysql.query_db(messages)

    comments = "SELECT comments.user_id, comment ,comments.created_at, messages.id from users JOIN messages on users.id = messages.user_id JOIN comments on messages.id = comments.message_id"
    session['comments'] = mysql.query_db(comments)
    return render_template('thewall.html')

@app.route('/add', methods=['POST'])
def add():
    query = "INSERT INTO messages(message, created_at, user_id) VALUES (:one, NOW(), :three)"
    data = {
        'one':request.form['message'],
        'three':session['logged'][0]['id']
    }
    print request.form['message']
    print session['logged'][0]['id']
    mysql.query_db(query,data)
    return redirect('/wall')
@app.route('/comment/<var>', methods=['POST'])
def comment(var):
    query = "INSERT INTO comments(message_id, comment, created_at, user_id) VALUES (:one, :two, NOW(), :four)"
    data = {
        'one':var,
        'two':request.form['comment'],
        'four':session['logged'][0]['id']
    }
    mysql.query_db(query,data)
    return redirect('/wall')

@app.route('/login', methods=['POST'])
def login():
    query = "SELECT * FROM `users` WHERE `email` = :one LIMIT 1"
    check = mysql.query_db(query,{'one' : request.form['em']})
    print request.form['pw']
    if check:
        if bcrypt.check_password_hash(check[0]['password'], request.form['pw']) == True:
            print "true"
            session['logged'] = check
            return redirect("/wall")
        else:
            print "false"
            flash('Invalid Password!')
            return redirect('/')
    else:
        flash('Invalid Email Address!')
        print "invalid Email"
        return redirect('/')

@app.route('/logout', methods = ['GET'])
def logout():
    session.pop('logged')
    return redirect('/')

@app.route('/registration', methods=['POST'])
def register():
    query = "SELECT * FROM `users` WHERE `email` = :one LIMIT 1"
    check = mysql.query_db(query,{'one' : request.form['em']})
    if check:
        flash('Email already in use')
        return redirect('/')
    test = True
    if len(request.form['fn']) < 2 or request.form['fn'].isalpha() == False:
        flash("First name must be at least 2 characters and contain only letters")
        test = False
    if len(request.form['ln']) < 2 or request.form['ln'].isalpha() == False:
        flash("Last name must be at least 2 characters and contain only letters")
        test = False
    if len(request.form['em']) < 1 or not EMAIL_REGEX.match(request.form['em']):
        flash("Must input valid Email address")
        test = False
    if len(request.form['pw']) < 8:
        flash("Password must be more than 8 characters")
        test = False
    if test == False:
        return redirect('/')


    password = bcrypt.generate_password_hash(request.form['pw'])
    query = "INSERT INTO `the_wall_db`.`users` (`first_name`,`last_name`,`email`,`password`,`created_at`) VALUES (:one, :two, :three, :four, NOW())"
    data = {'one' : request.form['fn'], 'two' : request.form['ln'], 'three' : request.form['em'], 'four' : password,}
    mysql.query_db(query,data)
    query = "SELECT * FROM `users` WHERE `email` = :one LIMIT 1"
    session['logged'] = mysql.query_db(query,{'one' : request.form['em']})
    print session['logged']
    return render_template('thewall.html')

# app.run(host="0.0.0.0")
app.run(debug = True)



# code=307
