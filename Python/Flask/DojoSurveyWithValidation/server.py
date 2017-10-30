from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'SECRET'
@app.route('/')

def index():
    # return "Index Page"
    return render_template('index.html')

@app.route('/result',methods=['POST'])
def result():
    if len(request.form['name'])< 1:
        flash('You forgot your name')
        return redirect('/')
    if len(request.form['comments'])< 1:
        flash("You didn't want to leave any comments?")
        return redirect('/')
    elif len(request.form['comments']) > 120:
        flash('That was too much text, you broke the box!')
        return redirect('/')
    else:
        name = request.form['name']
        location = request.form['location']
        comments= request.form['comments']
        language = request.form['language']
        return render_template('result.html',name = name, location= location, comments=comments,language=language)


app.run(debug=True)
