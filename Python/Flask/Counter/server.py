from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Secretive'
@app.route('/')
def index():

    try:
        session['count'] += 1
    except:
        session['count'] = 1
    return render_template('index.html')


    # session['count'] = 0
    # return redirect('/counting')
    # # return render_template('index.html')
@app.route('/add2', methods=['POST'])
def add2():
    session['count'] += 1
    return redirect('/')
@app.route('/reset_count', methods=['POST'])
def reset():
    session['count'] = 0
    return redirect('/')


app.run(debug=True)
