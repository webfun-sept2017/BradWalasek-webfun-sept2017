from flask import Flask, redirect, request, session, flash, render_template
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app,'email_validation_db')
app.secret_key='key'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():

    return render_template("index.html")
@app.route('/s', methods=["POST"])
def store():
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid Email')
        return render_template('index.html')
    else:
        email = request.form['email']
        # user = request.form['user']
        # print user
        print email
        query = "INSERT INTO users (email, createdat) VALUES (:two, NOW())"
        data = {
            # 'one' : user,
            'two' : email
        }
        mysql.query_db(query,data)
        return redirect ('/display')
@app.route('/display')
def end():
    messages = "SELECT * from users"
    print mysql.query_db(messages)
    session['print'] = mysql.query_db(messages)
    return render_template('display.html')
app.run(debug=True)
