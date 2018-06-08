from flaskr.app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import uuid
from random import randint
from flask import current_app
from base64 import b64encode, b64decode
import os

MSG_REC_SIZE = 512

def default_uuid():
    return str(uuid.uuid4())


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(64), unique=True)
    user_pass = db.Column(db.String(256))
    user_firstname = db.Column(db.String(64))
    user_lastname = db.Column(db.String(64))
    user_signature = db.Column(db.String(64))
    user_mailbox = db.Column(db.String(64), unique=True)

    def __init__(self, name=None, password=None, firstname=None, lastname=None, signature=None, mailbox=None, id=None):
        super().__init__()
        if id:
            self.id = id
        self.user_name = name
        self.user_pass = generate_password_hash(password)
        self.user_firstname = firstname
        self.user_lastname = lastname
        self.user_signature = signature
        self.user_mailbox = mailbox

    def change_password(self, password):
        self.user_pass = generate_password_hash(password)
        db.session.commit()

    def check_password(self, password):
        return check_password_hash(self.user_pass, password)

    def update_user(self, firstname=None, lastname=None, signature=None):
        self.user_firstname = firstname
        self.user_lastname = lastname
        self.user_signature = signature
        db.session.commit()

    @staticmethod
    def register_user(new_user):
        db.session.add(new_user)
        db.session.commit()

    def __repr__(self):
        return "<User(user_name='%s',  user_pass='%s', user_firstname='%s' user_lastname='%s')>" % (self.user_name, self.user_pass, self.user_firstname, self.user_lastname)

class Message:
    def __init__(self, src=None, dst=None, msg=None):
        self.msg_src = src
        self.msg_dst = dst
        self.msg_msg = msg

    def reload(self, new_msg):
        if len(new_msg) == MSG_REC_SIZE:
            self.msg_src = new_msg[0:36]
            self.msg_dst = new_msg[36:72]
            self.msg_msg = new_msg[72:MSG_REC_SIZE]

    def as_bytes(self):
        return bytes(self.msg_src + self.msg_dst + self.msg_msg, 'utf-8')

    def as_padded_bytes(self):
        output_str = self.msg_src + self.msg_dst + self.msg_msg
        total_len = len(output_str)
        if total_len > MSG_REC_SIZE:
            print("Message corruption imminent. Record Length (%d)" % total_len)
        elif total_len < MSG_REC_SIZE:
            output_str += ' '*(MSG_REC_SIZE-total_len)
            # print("Message padded to %d size." % len(output_str))

        return bytes(output_str, 'utf-8')

    def as_padded_string(self):
        output_str = self.msg_src + self.msg_dst + self.msg_msg
        total_len = len(output_str)
        if total_len > MSG_REC_SIZE:
            print("Message corruption imminent. Record Length (%d)" % total_len)
        elif total_len < MSG_REC_SIZE:
            output_str += ' '*(MSG_REC_SIZE-total_len)

        return output_str

    def send_msg(self):
        msg_bytes = self.as_padded_bytes()

        src_mailbox = None
        dst_mailbox = None
        if msg_bytes is not None and len(msg_bytes) == MSG_REC_SIZE:

            try:
                src_mailbox_name = b64encode(bytes(str(self.msg_src), 'utf-8')).decode('utf-8')
                filepath = os.path.join(current_app.config.get("APP_BASE_DIR"), src_mailbox_name + ".txt")
                src_mailbox = open(filepath, "ab")

                dst_mailbox_name = b64encode(bytes(str(self.msg_dst), 'utf-8')).decode('utf-8')
                filepath = os.path.join(current_app.config.get("APP_BASE_DIR"), dst_mailbox_name + ".txt")
                dst_mailbox = open(filepath, "ab")
            except Exception as e:
                print(str(e))
                return False
        else:
            print("Byte Len Mismatch: %d" % len(msg_bytes))
            return False


        src_mailbox.write(msg_bytes)
        dst_mailbox.write(msg_bytes)

        ### Begin greeter Code
        if self.msg_dst == current_app.config.get("GREETER"):
            tmp = self.msg_src
            self.msg_src = self.msg_dst
            self.msg_dst = tmp

            GREETER_MSGS = current_app.config.get("GREETER_MSGS")
            msg = GREETER_MSGS[randint(0, len(GREETER_MSGS)-1)]
            self.msg_msg = msg
            resp_bytes = self.as_padded_bytes() # needed the recipients swapped

            src_mailbox.write(resp_bytes) # Open mailbox never changed.
        ### End greeter code.

        # Close mailboxes
        src_mailbox.close()
        dst_mailbox.close()

        return True

    def msg_size(self):
        return len(self.msg_src + self.msg_dst + self.msg_msg)

    def __repr__(self):
        return self.msg_src + self.msg_dst + self.msg_msg

