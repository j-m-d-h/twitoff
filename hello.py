"""Minimal flask app"""

from flask import Flask

# make app
app = Flask(__name__)

# make route
@app.route("/")

# define function
def hello():
    return "Greetings."
