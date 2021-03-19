from app import app 
from app import models
from app import forms
from flask import render_template, request, redirect, url_for, flash


@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/nav')
def ar():
    """Render camera with ar experience  <19/3/2021 N.Bedassie>"""
    return render_template("map.html")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")