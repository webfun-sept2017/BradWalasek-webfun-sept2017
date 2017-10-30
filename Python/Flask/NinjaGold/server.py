from flask import Flask, render_template, session, redirect, request
import random
import datetime
app=Flask(__name__)
app.secret_key="key"

@app.route('/')
def main():

    try:
        session['gold']
    except:
        session['gold'] = 0

        session['loc'] = ''
        session['m'] = 0;

        session['arr'] = []
        session['count'] = 0

    return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def money():

    if request.form['location'] == "farm":
        session['m'] = random.randint(10,20)
        session['gold'] = session['m'] + int(session['gold'])
        session['arr'].insert(0,("You have earned " + str(session['m']) + " gold at the Farm"))
        session['count'] = int(session['count']) +1
    elif request.form['location'] == "cave":
        session['m']= random.randint(5,10)
        session['gold'] = session['m'] + int(session['gold'])
        session['arr'].insert(0,("You have earned " + str(session['m']) + " gold at the Cave"))
        session['count'] = int(session['count']) +1
    elif request.form['location'] == "house":
        session['m'] = random.randint(2,5)
        session['gold'] = session['m'] + int(session['gold'])
        session['arr'].insert(0,("You have earned " + str(session['m']) + " gold at the House"))
        session['count'] = int(session['count']) +1
    else:
        session['m'] = random.randint(-50, 50)
        session['gold'] = session['m'] + int(session['gold'])
        session['arr'].insert(0,("You have earned " + str(session['m']) + " gold at the Casino"))
        # session['arr'][session["count"]]= "You have earned " + str(session['m']) + " gold at the Casino"
        session['count'] = int(session['count']) +1
    return redirect('/')


@app.route('/reset',methods=['POST'])
def reset():
    session.pop('gold')
    session.pop('loc')
    return redirect('/')
app.run(debug=True)
