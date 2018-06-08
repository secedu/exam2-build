from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uuid import FlaskUUID

db = SQLAlchemy()
flask_uuid = FlaskUUID()
flask_login = LoginManager()

from flaskr.models import User, Trash
from flaskr.controllers.main import main
from datetime import datetime, timedelta
import random
import string
import os
import re

app = Flask(__name__)


def randstr(n):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))


class ConfigClass(object):
    DEBUG = True
    SECRET_KEY = 'Has Anyone Really Been Far Even as Decided to Use Even Go Want to do Look More Like Exam?'
    SQL_ROOT_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD", "")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:{}@{}/db'.format(SQL_ROOT_PASSWORD, DB_HOST)
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    HOST = os.getenv("HOST", "http://localhost")
    FLAG = os.getenv("FLAG", "flag{testing123}")


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


def post_trash(user, delta, public, title, content):
    db.session.add(Trash(author=user, timestamp=datetime.utcnow()-timedelta(days=delta), is_public=public,
                         title=title, content=content, highlight='no-highlight', password=''))
    db.session.commit()
    db.session.flush()


def populate_db(app):
    with app.app_context():

        if len(Trash.query.all()) > 0:
            return

        admin = User(username='admin')
        admin.set_password(randstr(64))

        user = User(username='thementor')
        user.set_password(randstr(64))

        db.session.add(admin)
        db.session.add(user)
        db.session.commit()

        post_trash(admin, 1, False, 'You Found Me!', app.config.get("FLAG"))
        post_trash(admin, 2, True, 'Get some Lorem Ipsum', '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.''')
        post_trash(user, 3, True, 'The Conscience of a Hacker', '''        Another one got caught today, it's all over the papers.  "Teenager
Arrested in Computer Crime Scandal", "Hacker Arrested after Bank Tampering"...
        Damn kids.  They're all alike.

        But did you, in your three-piece psychology and 1950's technobrain,
ever take a look behind the eyes of the hacker?  Did you ever wonder what
made him tick, what forces shaped him, what may have molded him?
        I am a hacker, enter my world...
        Mine is a world that begins with school... I'm smarter than most of
the other kids, this crap they teach us bores me...
        Damn underachiever.  They're all alike.

        I'm in junior high or high school.  I've listened to teachers explain
for the fifteenth time how to reduce a fraction.  I understand it.  "No, Ms.
Smith, I didn't show my work.  I did it in my head..."
        Damn kid.  Probably copied it.  They're all alike.

        I made a discovery today.  I found a computer.  Wait a second, this is
cool.  It does what I want it to.  If it makes a mistake, it's because I
screwed it up.  Not because it doesn't like me...
                Or feels threatened by me...
                Or thinks I'm a smart ass...
                Or doesn't like teaching and shouldn't be here...
        Damn kid.  All he does is play games.  They're all alike.

        And then it happened... a door opened to a world... rushing through
the phone line like heroin through an addict's veins, an electronic pulse is
sent out, a refuge from the day-to-day incompetencies is sought... a board is
found.
        "This is it... this is where I belong..."
        I know everyone here... even if I've never met them, never talked to
them, may never hear from them again... I know you all...
        Damn kid.  Tying up the phone line again.  They're all alike...

        You bet your ass we're all alike... we've been spoon-fed baby food at
school when we hungered for steak... the bits of meat that you did let slip
through were pre-chewed and tasteless.  We've been dominated by sadists, or
ignored by the apathetic.  The few that had something to teach found us will-
ing pupils, but those few are like drops of water in the desert.

        This is our world now... the world of the electron and the switch, the
beauty of the baud.  We make use of a service already existing without paying
for what could be dirt-cheap if it wasn't run by profiteering gluttons, and
you call us criminals.  We explore... and you call us criminals.  We seek
after knowledge... and you call us criminals.  We exist without skin color,
without nationality, without religious bias... and you call us criminals.
You build atomic bombs, you wage wars, you murder, cheat, and lie to us
and try to make us believe it's for our own good, yet we're the criminals.

        Yes, I am a criminal.  My crime is that of curiosity.  My crime is
that of judging people by what they say and think, not what they look like.
My crime is that of outsmarting you, something that you will never forgive me
for.

        I am a hacker, and this is my manifesto.  You may stop this individual,
but you can't stop us all... after all, we're all alike.

                               +++The Mentor+++''')


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


def xss_filter(input, pattern, case_sensitive):
    if case_sensitive:
        return input.replace(pattern, '')
    else:
        regex = re.compile(pattern, re.IGNORECASE)
        return regex.sub('', input)


@app.template_filter('xss_1')
def xss_1(s):
    s = xss_filter(s, 'script', False)
    s = xss_filter(s, 'document', False)
    return s


@app.template_filter('xss_2')
def xss_2(s):
    s = xss_filter(s, 'img', False)
    s = xss_filter(s, 'src', False)
    s = xss_filter(s, 'location', False)
    return s


@app.template_filter('xss_3')
def xss_3(s):
    s = xss_filter(s, 'onerror', True)
    return s


@app.template_filter('xss_4')
def xss_4(s):
    s = xss_filter(s, 'onload', True)
    return s


@app.template_filter('xss_5')
def xss_5(s):
    return s


@app.template_filter('xss_6')
def xss_6(s):
    #s = xss_filter(s, '//', True)
    s = xss_filter(s, '/*', True)
    return s

