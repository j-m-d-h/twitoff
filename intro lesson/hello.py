"""Minimal flask app"""

from flask import Flask, render_template

# make app
app = Flask(__name__)

# make route
@app.route("/")

# define function
def hello():
    return render_template('home.html')

# make second route
@app.route("/about")

# define about function
def thing():
    return render_template('about.html')
