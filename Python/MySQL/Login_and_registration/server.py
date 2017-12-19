from flask import Flask, redirect, request, render_template, flash, session
from mysqlconnection import MySQLConnector
import md5
import os, binascii
import re
from flask_bcrypt import Bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app=Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'login_and_registration_db')
app.secret_key="secret"
@app.route('/')
def index():
    try:
        return render_template('success.html')
    except:
        return render_template('index.html')
@app.route('/login', methods=['POST'])
def login():

    query = "SELECT * FROM `users` WHERE `email` = :one LIMIT 1"
    check = mysql.query_db(query,{'one' : request.form['em']})
    if check:
        print request.form['pw']

        if bcrypt.check_password_hash(check[0]['password'], request.form['pw']) == True:
            print "true"
            session['logged'] = check
            return render_template("success.html")
        else:
            print "false"
            flash('Invalid Password!')
            return redirect('/')
    else:
        flash('Invalid Email Address!')
        print "invalid Email"
        return redirect('/')
@app.route('/add', methods=['POST'])
def add():
    # validation steps
# First Name - letters only, at least 2 characters and that it was submitted
# Last Name - letters only, at least 2 characters and that it was submitted
# Email - Valid Email format, and that it was submitted
# Password - at least 8 characters, and that it was submitted
# Password Confirmation - matches password
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
    # salt =  binascii.b2a_hex(os.urandom(15))
    # password = md5.new(request.form['pw'] + salt).hexdigest();
    query = "INSERT INTO `login_and_registration_db`.`users` (`first_name`,`last_name`,`email`,`password`,`created_at`) VALUES (:one, :two, :three, :four, NOW())"
    data = {'one' : request.form['fn'], 'two' : request.form['ln'], 'three' : request.form['em'], 'four' : password,}
    mysql.query_db(query,data)
    query = "SELECT * FROM `users` WHERE `email` = :one LIMIT 1"
    session['logged'] = mysql.query_db(query,{'one' : request.form['em']})
    print session['logged']
    return render_template('success.html')
@app.route('/logout')
def logout():
    session.pop('logged')
    return redirect('/')
app.run(debug=True)
