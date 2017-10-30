from flask import Flask, redirect, request, session, render_template, flash
from mysqlconnections import MySQLConnector
app=Flask(__name__)
app.secret_key = "Meh"
mysql = MySQLConnector(app,"the_wall_db")
@app.route('/')
def index():
    try:
        session['logged']
        return render_template('thewall.html')
    except:
        return render_template('index.html')

@app.route('/wall', methods= ['POST'])
# @app.route('/wall', methods= ['GET'])
def wall():

# |||||   \\\                       //
#  |||     \\                      //
#  |||      \\        //\\        //
#  |||       \\      //  \\      //
#  |||        \\    //    \\    //
#  |||         \\  //      \\  //
# |||||          \\//       \\//


    if request.form['message']:
        query = "INSERT INTO messages(message, user_id) VALUES (:one, :two)"
        data = {
            'one':request.form['message'],
            'two':session['id']
        }
        mysql.query_db(query,data)
    messages = "SELECT message from messages WHERE user_id = :one"
    data = {
        'one' : session['id']
    }
    session['print'] = mysql.query_db(messages, data)
    # for count in range(0, len(session['print'])):
    #     print session['print'][count]['message']
    return render_template('thewall.html')



@app.route('/login', methods=['POST'])
def login():
    user=request.form['user']
    password=request.form['password']
    print user
    print password
    queryu = ("SELECT first_name FROM users WHERE first_name = :one ")
    queryp = ("SELECT password FROM users WHERE first_name = :one ")
    data = {
        'one' : user
    }

    print mysql.query_db(queryu, data)[0]['first_name']
    try:
        if user == mysql.query_db(queryu, data)[0]['first_name']:
            if password == mysql.query_db(queryp, data)[0]['password']:
                session['logged'] = user
                query =("SELECT id FROM users WHERE first_name = :one ")
                data = {
                    'one' : user
                }
                session['id'] = mysql.query_db(query, data)[0]['id']
                print mysql.query_db(query, data)[0]['id']

                messages = "SELECT message from messages WHERE user_id = :one"
                data = {
                    'one' : session['id']
                }
                session['print'] = mysql.query_db(messages, data)



                return render_template('thewall.html')
            else:
                flash("Invalid password")
        return redirect('/')
    except:
        flash("Invalid user")
        return redirect('/')
@app.route('/logout', methods = ['GET'])
def logout():
    session.pop('logged')
    session.pop ('id')
    try:
        session.pop('print')
    except:
        print 'nothing in session["print"]'
    return redirect('/')

@app.route('/registration', methods=['POST'])
def register():

    query = "INSERT INTO users (first_name, last_name, email, password) VALUES (:first_name,:last_name,:email, :password)"
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : request.form['password']
    }
    mysql.query_db(query,data)
    flash('Account created!')
    return redirect('/')
app.run(debug=True)



# code=307
