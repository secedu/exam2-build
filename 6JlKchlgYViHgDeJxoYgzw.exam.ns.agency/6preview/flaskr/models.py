from flaskr.app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import hashlib


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    is_admin = db.Column(db.Boolean(), default=False)
    passhash = db.Column(db.String(128))
    reset_q = db.Column(db.String(1024))
    reset_a = db.Column(db.String(1024))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.passhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passhash, password)

    def check_reset(self, response, token):

        return self.reset_a == response


    def is_authenticated(self):
        return self.id > 0


class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    subject = db.Column(db.String(1024))
    body = db.Column(db.String(1024))

    def __repr__(self):
        return '<Email {}>'.format(self.subject)
