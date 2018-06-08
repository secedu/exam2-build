from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uuid import FlaskUUID

db = SQLAlchemy()
flask_uuid = FlaskUUID()
flask_login = LoginManager()

from flaskr.models import User, Message
from flaskr.controllers.main import main
from datetime import datetime, timedelta
from base64 import b64decode, b64encode
import os
import re

app = Flask(__name__)

# docker run -p 3306:3306 d11wtq/mysql
MSG_REC_SIZE = 512

class ConfigClass(object):
    DEBUG = True
    SECRET_KEY = 'wubba lubba dub dub!'
    SQL_ROOT_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD", "")
    DB_HOST = os.getenv("DB_HOST", "mysql")
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:{}@{}/db'.format(SQL_ROOT_PASSWORD, DB_HOST)
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    HOST = os.getenv("HOST", "http://localhost")
    FLAG = os.getenv("FLAG", "flag{testing123}")
    FLAG1 =  'flag{4ll_d4y_4l1_n1gh7_s1Ggie5}'
    APP_BASE_DIR = os.path.dirname(__file__)
    MSG_REC_SIZE = MSG_REC_SIZE

    GREETER =   '4badd00d-d11d-4bad-1dea-c001fac3db01'
    ADMIN =     '94476441-6443-9242-6445-c001fac3d00d'
    GREETER_MSGS = [ "Oh hey bud. What's good?",
                    "I hope you have had a good time in the course this year.",
                    "I had a lot of fun creating labyrinths for you.",
                    "Do try to be gentle on yourself and your peers.",
                    "Take your failures with grace, know what leads you to failure.",
                    "Have direct relationships with people if you want good relationships.",
                    "We encourage you to participate in CTFs and come to conferences with us!",
                    "Thanks for listening to us rant.",
                    "Good luck in the exam! Don't be discouraged.",
                    "Take deep breaths from time to time. Be courageous.",
                    "Your marks should only say as much as the truth that 'You have much to improve upon.'",
                    "A secure society isn't a human one. The expression of vulnerability is an important requirement for modern mankind.",
                    "You should read The Art of War by Sun Tzu. War is the consequence of human nature.",
                    "You should read Ready Player One. It's a blast, treat yourself!",
                    "I am actually a mechanical turk.",
                    "No, there's no flag in my message list. You don't need to try to find one."]


def register_models(app):
    with app.app_context():

        flask_login.login_view = '.login'

        flask_uuid.init_app(app)
        flask_login.init_app(app)

        db.init_app(app)
        db.drop_all()
        db.create_all()


def register_blueprints(app):
    app.register_blueprint(main)


def populate_db(app):
    with app.app_context():

        if len(User.query.all()) > 0:
            return

        users = [
            ('noone', 'noone_can_know', 'noone', 'dodgy', 'Im not who you are looking for', '4badd00d-d11d-4bad-1dea-c001fac3db01', 1),
            ('admin', 'noone_can_know', 'noone', 'dodgy', 'Im not who you are looking for', '4badd01d-d11d-4bad-1dea-c001fac3db01', 2),
            ('Sketch', 'temporary', 'Someone', 'Sketchy', 'Salutations, friend.', 'defec7ed-c001-face-d00d-313333333337', 1337),
            # removed flag beyond spec
            # ('ENUMFLAG{f1nD1nG_bUrIeD_tReAsUrE}', 'temporary', 'Ooops!', 'My', "u R hired. grats Worth nothing.", '64436443-6443-6443-6443-644364436443', 6443),
            ('4dm1ni5trator', 'temporary', 'Damo', 'Daz', app.config.get("FLAG1"), '94476441-6443-9242-6445-c001fac3d00d', 9447),
            ('Carey', 'temporary', 'Carey', 'Spice', '*crickets*', '01010101-0101-0101-0101-010101010101', 13337),
        ]
        for user in users:
            new_user = User(*user)
            db.session.add(new_user)

        db.session.commit()

        ADMIN = current_app.config.get("ADMIN")
        GREETER = current_app.config.get("GREETER")

        a = User.query.filter_by(user_name='4dm1ni5trator').first()
        n = User.query.filter_by(user_name='noone').first()

        if a is not None:
            # Set and touch admin mailbox.
            a.change_password('administrator')
            mailbox_name = b64encode(bytes(ADMIN, 'utf-8')).decode('utf-8')
            mailbox_path = os.path.join( current_app.config.get("APP_BASE_DIR"), 'mailbox', mailbox_name + '.txt')
            fp = open(mailbox_path, "wb")
            fp.close()
        else:
            print("shit")
            raise(NameError("Failed"))


        new_msg = Message(ADMIN, GREETER, 'Greeter, can you give me the flag?.')
        success = new_msg.send_msg()
        new_msg = Message(GREETER, ADMIN, 'Noone is the boss of me.')
        success = new_msg.send_msg()
        new_msg = Message(ADMIN, GREETER, "Fine, I'll send it to myself then!")
        success = new_msg.send_msg()
        new_msg = Message(ADMIN, ADMIN, 'flag{411_53e1ng_eYe}')
        success = new_msg.send_msg()

def create_app():
    global app
    app.config.from_object(__name__ + '.ConfigClass')
    register_models(app)
    register_blueprints(app)
    populate_db(app)
    return app


@flask_login.user_loader
def load_user(id):
    return User.query.get(int(id))


