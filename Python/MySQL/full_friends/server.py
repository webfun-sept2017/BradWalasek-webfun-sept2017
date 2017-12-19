from flask import Flask, redirect, flash, request, session, render_template
from mysqlconnection import MySQLConnection
app = Flask(__name__)
app.secret_key = "Secret"
mysql = MySQLConnection(app, "full_friends_db")
@app.route('/')
def index():


    query = "SELECT * FROM full_friends_db.friends;"

    session['print'] = mysql.query_db(query)
    return render_template('index.html')

@app.route('/friends', methods = ["POST"])
def storing():
    # return "/store works"
    first = request.form['first']
    last = request.form['last']
    email = request.form['email']
    print first + last + email
    # return redirect('/')



    query = "INSERT INTO `full_friends_db`.`friends` (`firstname`, `lastname`, `email`) VALUES (:one, :two, :three);"
    data = {
        'one' : first,
        'two' : last,
        'three' : email
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<var>/delete', methods=['POST'])
def delete(var):
    query = "DELETE FROM `full_friends_db`.`friends` WHERE id = :one"
    data = {
        "one" : var
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<var>/edit', methods=['GET'])
def edit(var):
    query = "SELECT * FROM `full_friends_db`.`friends` WHERE id = :one"
    data = {
        "one" : var
    }
    session['print'] = mysql.query_db(query, data)
    return render_template("edit.html")
@app.route('/friends/<var>', methods= ['POST'])
def update(var):
    query = "UPDATE `full_friends_db`.`friends` SET `firstname` = :one, `lastname` = :two, `email` = :three WHERE id = :four"
    data = {
        "one" : request.form['first'],
        "two" : request.form['last'],
        "three" : request.form['email'],
        "four" : var
    }
    mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True)
