from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')

def front_page():
    # return "Hello World!"
    return render_template('index.html')

@app.route('/ninjas')
def ninjapage():
    # return "Ninjas!"
    return render_template('ninjas.html')

@app.route('/dojos/new')
def signUp():
    # return "This is the form!"
    return render_template('dojos.html')





app.run(debug=True)
