from flask import Flask, render_template

@app.route('/')
def home():
    try:
        return render_template('home.html')
