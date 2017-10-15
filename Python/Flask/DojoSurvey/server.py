from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    # return "Index Page"
    return render_template('index.html')

@app.route('/result',methods=['POST'])
def result():
    name = request.form['name']
    location = request.form['location']
    comments= request.form['comments']
    language = request.form['language']
    return render_template('result.html',name = name, location= location, comments=comments,language=language)


app.run(debug=True)
