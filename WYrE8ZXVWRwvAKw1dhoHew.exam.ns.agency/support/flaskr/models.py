from flaskr.app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import uuid


def default_uuid():
    return str(uuid.uuid1())


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True, unique=True)
    passhash = db.Column(db.String(255))
    trash = db.relationship('Trash', backref='author', lazy='dynamic', order_by="desc(Trash.idx)")

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.passhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passhash, password)


def default_trash_index():
    return Trash.query.count() + 1


class Trash(db.Model):
    uuid = db.Column(db.String(64), primary_key=True, default=default_uuid)
    idx = db.Column(db.Integer(), default=default_trash_index)
    views = db.Column(db.Integer(), default=0)
    title = db.Column(db.String(4096))
    content = db.Column(db.String(4096))
    highlight = db.Column(db.String(4096))
    password = db.Column(db.String(4096))
    is_public = db.Column(db.Boolean())
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Trash {}>'.format(self.uuid)