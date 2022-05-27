from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/blogs')
def blogs():
    return render_template('blogs.html')
