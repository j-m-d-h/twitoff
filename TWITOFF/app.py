"""Code for our app"""

from flask import Flask, render_template, request
from .models import DB, User
from decouple import config

# make app factory

def create_app():
    app = Flask(__name__)

    # add config for database
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')

    # stop tracking modifications warning
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # show the database the app
    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html', title = 'Home', users=users)

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title = 'Reset', users=[])

    return app
