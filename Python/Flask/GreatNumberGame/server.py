from flask import Flask, redirect, request, session, render_template
import random
app = Flask(__name__)
app.secret_key = "Secret"


@app.route('/')
def init():
    try:
        session['number']
    except:
        session['number'] = random.randint(0,10)
        session['color'] = 'white'

    return render_template('index.html')


@app.route('/calc', methods=['POST'])
def compare():

    try:
        if int(request.form['guess']) == int(session['number']):
            session['test']= 'Success!'
            session['color'] = 'green'
        elif int(request.form['guess']) < int(session['number']):
            session['test']= 'Too Low'
            session['color'] = 'red';
        else:
            session['test']= 'Too high'
            session['color'] = 'red'
    except:
        session['test']="There wasn't a valid guess!"


    return redirect('/')
@app.route('/reset', methods=["POST"])
def reset():
    session.pop('number')
    session.pop('test')
    return redirect('/')








app.run(debug=True)










    # try:
    #     if request.form('guess') != session['number']:
    #         session['response'] = "nope!"
    #     if request.form('guess') == session['number']:
    #         session['response'] = "yep!"
    # except:
    #     session['number'] = random.randint(1,100)
