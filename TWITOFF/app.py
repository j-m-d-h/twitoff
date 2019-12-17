"""Code for our app"""

from flask import Flask
from .models import DB

# make app factory

def create_app():
    app = Flask(__name__)

    # add config for database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    # show the database the app
    DB.init_app(app)
    
    @app.route('/')
    def root():
        return 'Welcome to Twitoff'
    return app
