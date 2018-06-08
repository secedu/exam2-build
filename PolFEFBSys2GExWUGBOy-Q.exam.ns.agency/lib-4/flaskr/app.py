from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import string
import random
import os

db = SQLAlchemy()

from flaskr.models import User, Email
from flaskr.controllers.main import main

app = Flask(__name__)


class ConfigClass(object):
    DEBUG = True
    SECRET_KEY = 'Has Anyone Really Been Far Even as Decided to Use Even Go Want to do Look More Like Exam?'
    SQL_ROOT_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD", "")
    SQL_HOST = os.getenv("DB_HOST", "localhost")
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:{}@{}/db'.format(SQL_ROOT_PASSWORD, SQL_HOST)
    #SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    HOST = os.getenv("HOST", "http://localhost")
    FLAG = os.getenv("FLAG", "flag{testing123}")


def randstr(n):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))


def register_models(app):
    with app.app_context():
        db.init_app(app)
        db.drop_all()
        db.create_all()


def register_blueprints(app):
    app.register_blueprint(main)


def populate_db(app):
    with app.app_context():

        if len(User.query.all()) > 0:
            return

        admin = User(username='admin', is_admin=True, reset_q='The place I put that thing one time.', reset_a=randstr(64))

        admin.set_password('password')

        guest = User(username='guest', reset_q='My favourite place of learning!', reset_a='unsw')
        guest.set_password('guest')

        azured = User(username='azured', reset_q='All I see is...', reset_a='*******')
        azured.set_password('hunter2')

        mail = Email(subject='Welcome to LMail', body='Email we send to you will appear in this inbox!')

        db.session.add(admin)
        db.session.add(guest)
        db.session.add(azured)
        db.session.add(mail)
        db.session.commit()


def create_app():
    global app
    app.config.from_object(__name__ + '.ConfigClass')
    register_models(app)
    register_blueprints(app)
    populate_db(app)
    return app
