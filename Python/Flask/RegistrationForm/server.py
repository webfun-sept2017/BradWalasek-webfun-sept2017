from flask import Flask, render_template, request, redirect, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "secret"
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/reg', methods=["POST"])
def registration():
    first = request.form['first']
    last = request.form['last']
    email = request.form['email']
    password = request.form['password']
    passwordconfirm = request.form['passwordconfirm']
    print first
    print last
    print email
    print password
    print passwordconfirm
    passed = True
    if first.isalpha() == False:
        flash("First name must contain no numbers or symbols!")
        passed = False
    if last.isalpha() == False:
        flash("Last name must contain no numbers or symbols!")
        passed = False
    if len(first) < 1 or len(last) < 1 or len(email)<1 or len(password)<1 or len(passwordconfirm) < 1:
        flash("Must enter values in all fields!")
        passed = False
    if len(password) < 9:
        flash("Password must be more than 8 characters!")
        passed = False
    if password != passwordconfirm:
        flash("Passwords must match!")
        passed = False
    if not EMAIL_REGEX.match(email):
        flash("Invalid Email!")
        passed = False
    if passed == True:
        flash('Thank you for submitting your information!')
        return redirect('/')
    else:
        return redirect('/')
app.run(debug=True)
