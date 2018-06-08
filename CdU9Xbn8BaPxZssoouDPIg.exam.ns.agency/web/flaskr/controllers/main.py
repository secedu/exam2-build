from flask import Blueprint, render_template, request, render_template_string, current_app, flash, redirect, url_for, session
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
import re
import json
import os
from datetime import datetime
from uuid import uuid4
from base64 import b64encode, b64decode

from flaskr.app import db
from flaskr.forms import LoginForm, RegisterForm, ModifyForm, SendMsgForm
from flaskr.models import User, Message

main = Blueprint('main', __name__)

@main.errorhandler(404)
def page_not_found(error):
    return '404 page not found', 404


@main.route('/')
def home():
    return render_template('pages/index.html')

# Terms and Conditions
@main.route('/terms', methods=["GET"])
def terms():
    return render_template('pages/terms.html')

@main.route('/robots.txt')
def robots():
    resp = make_response('''
User-agent: *
Disallow: /whois
''')
    resp.mimetype = "text/plain"
    return resp

@main.route('/whois', methods=["GET"])
def who_is():
    target = None
    if 'id' in request.args:
        try:
            target = int(request.args['id'])
        except:
            return "400 Bad Request (id could not be cast)"
    else:
        return "400 Bad Request (id empty)"

    if target is not None:
        User.query.all()
        user = User.query.filter_by(id=target).first()
        if user is None:
            return '404 Not Found', 404
        else:
            return user.user_name, 200

# User Login
@main.route('/login', methods=["POST","GET"])
def login():
    # Redirect Logged In Users
    if session.get('logged_in'):
        return redirect('/user')

    error = None
    if request.method == 'GET':
        form = LoginForm(request.form)
        return render_template('forms/login.html', form=form)
    else:
        if 'name' in request.form and 'password' in request.form:
            User.query.all()
            user = User.query.filter_by(user_name=request.form['name']).first()

            if user is not None:
                if user.check_password(request.form['password']):
                    error = 'Password Matched'
                    login_user(user)
                    session['logged_in'] = True
                    session['user_name'] = user.user_name
                    session['user_id'] = user.id

                    flash('Login Successful')
                    return redirect('/user')
                else:
                    error = 'Login Failed'
            else:
                error = 'Login Failed'

            form = LoginForm(request.form)
            return render_template('forms/login.html', form=form, err=error)
        else:
            form = LoginForm(request.form)
            return render_template('forms/login.html', form=form, err=True)

@main.route('/logout')
def logout():
    logout_user()
    session['logged_in'] = False
    flash('Logout Successful')
    return redirect('/login')

# User Information Functionality.
@main.route('/user', methods=["GET"])
def users():

    if not session.get('logged_in'):
        return redirect('/')

    form = ModifyForm()
    User.query.all()
    user = User.query.filter_by(user_name=session['user_name']).first()
    if user is not None:
        form.firstname.data = user.user_firstname
        form.lastname.data = user.user_lastname
        form.signature.data = user.user_signature
    return render_template('pages/users.html', form=form)

@main.route('/user/<int:userid>', methods=["GET", "POST"])
def users_data(userid):
    if not session.get('logged_in'):
        return redirect('/')


    name = session['user_name']
    form = ModifyForm(request.form)

    firstname = None
    lastname = None
    signature = None

    creds = {}
    if request.method == "GET":
        User.query.all()
        user = User.query.filter_by(id=userid).first()
        if user is not None:

            if user.user_name == name:
                username = user.user_name
                mailbox = user.user_mailbox
                signature = user.user_signature
                firstname = user.user_firstname
                lastname = user.user_lastname

                creds.update({'User Name':username})
                creds.update({'Mailbox':mailbox})
                creds.update({'First Name':firstname})
                creds.update({'Last Name':lastname})
                creds.update({'Signature':signature})

            form.firstname.data = firstname
            form.lastname.data = lastname

    return render_template('lists/view.html', list=creds)

@main.route('/modify/<int:userid>', methods=["GET","POST"])
def user_modify(userid):
    if not session.get('logged_in'):
        return redirect('/')

    User.query.all()
    user = User.query.filter_by(id=userid).first()
    if user is not None:
        if request.method == "GET":
            form = ModifyForm()
            if user.user_name == session['user_name']:
                form = ModifyForm()
                form.firstname.data = user.user_firstname
                form.lastname.data = user.user_lastname
                form.signature.data = user.user_signature
                return render_template('forms/modify.html', form=form)
            else:
                return '403 Permission Denied', 403

        elif request.method == "POST":
            User.query.all()
            user = User.query.filter_by(id=userid).first()

            # Only update if we are the account owner
            if session['user_name'] == user.user_name:
                req_data = request.form['firstname']
                firstname = request.form['firstname']
                lastname = request.form['lastname']
                signature = request.form['signature']

                # Update the User
                user.update_user(firstname, lastname, signature)
                flash('You successfully updated your information!')
            return redirect('/user')
    else:
        return redirect('/')

## Messaging Routes
@main.route('/message/view', methods=["GET"])
def view_messages():
    if not session.get('logged_in'):
        return redirect('/')

    User.query.all()
    user = User.query.filter_by(user_name=session['user_name']).first()
    mailkey = None
    if user is not None:
        mailkey = b64encode(bytes(user.user_mailbox, 'utf-8')).decode('utf-8')
    return render_template('pages/message.html', mailkey=mailkey)

@main.route('/message/history', methods=["GET"])
def show_messages():
    # Kickout Scrubs
    if not session.get('logged_in'):
        return redirect('/')


    mailbox = None
    error = None
    User.query.all()
    name = session['user_name']
    sess_user = User.query.filter_by(user_name=name).first()
    if sess_user is None:
        return '403 Permission Denied', 403


    # Bail out on non standard requests.
    if 'v' in request.args:
        try:
            mailbox = request.args['v']
            mailbox_dec = b64decode(mailbox).decode('utf-8')
            print("Mailbox Decoded: {}".format(mailbox_dec))
            mailbox_owner = User.query.filter_by(user_mailbox=mailbox_dec).first()
            if mailbox_owner is None:
                return '400 Bad Request', 400

            


        except:
            error = "Cannot base64 decrypt value."
            return render_template('lists/history.html', err=error)
    else:
        error = "No mailkey provided."
        return render_template('lists/history.html', err=error)

    filepath = os.path.join(current_app.config.get("APP_BASE_DIR"), mailbox  + ".txt")
    fp = open(filepath, "r")

    MSG_REC_SIZE = current_app.config.get("MSG_REC_SIZE")
    msg_block = fp.read(MSG_REC_SIZE)
    msg_obj = Message()
    msgs = []

    while len(msg_block) == MSG_REC_SIZE:
        msg_obj.reload(msg_block)
        msg_str = msg_obj.as_padded_string()
        src = msg_str[0:36]
        dst = msg_str[36:72]
        msg = msg_str[72:MSG_REC_SIZE]


        src_user = User.query.filter_by(user_mailbox=src).first()
        dst_user = User.query.filter_by(user_mailbox=dst).first()
        tmp = {}
        if src_user is not None:
            tmp.update({'src':src_user.user_name})
            tmp.update({'srcbox':src})
        else:
            tmp.update({'src':src})

        if dst_user is not None:
            tmp.update({'dst':dst_user.user_name})
            tmp.update({'dstbox':dst})
        else:
            tmp.update({'dst':dst})

        tmp.update({'msg':msg.rstrip(' ')})
        msgs.append(tmp)

        msg_block = fp.read(MSG_REC_SIZE)

    fp.close()

    # Generate Message Form
    form = SendMsgForm(request.form)
    return render_template('lists/history.html', msgs=msgs[::-1], form=form)

@main.route('/message/send', methods=["POST"])
def send_message():
    # Kickout Scrubs
    if not session.get('logged_in'):
        return redirect('/')

    name = session['user_name']
    User.query.all()

    src_user = User.query.filter_by(user_name=name).first()

    if src_user is None:
        flash("User mailbox not found")
        return redirect('/')
    src_mailbox = src_user.user_mailbox
    mailkey = b64encode(bytes(str(src_mailbox), 'utf-8')).decode('utf-8')

    # Check target is valid
    target = request.form['mailbox']
    dst_user = User.query.filter_by(user_mailbox=target).first()
    if dst_user is None:
        flash("User mailbox not found")
        return redirect('/message/history?v=' + mailkey)
    dst_mailbox = dst_user.user_mailbox

    message = request.form.get("message", '')
    message = request.form['message']


    # Craft the message and send it.
    new_msg = Message(src_mailbox, dst_mailbox, message)
    success = new_msg.send_msg()
    if not success:
        flash("Message failed to send")
        return redirect('/message/history?v=' + mailkey)
    else:
        # Success
        return redirect('/message/history?v=' + mailkey)

# User Registration
@main.route('/register', methods=["POST","GET"])
def register():
    form = RegisterForm(request.form)
    error = None
    if request.method == "POST":
        if 'name' in request.form and 'password' in request.form:
            User.query.all()
            user = User.query.filter_by(user_name=request.form['name']).first()
            if user is None:
                uid = uuid4()
                # Create User
                new_user = User(request.form['name'], request.form['password'], 'Alice', 'Anonymous', 'iDont Facegood, literally iDont Even. lol! #6443_EXAM_MEME', str(uid) )
                User.register_user(new_user)

                # Create User Mailbox
                mailbox_name = b64encode(bytes(str(uid), 'utf-8')).decode('utf-8')
                filepath = os.path.join(current_app.config.get("APP_BASE_DIR"), mailbox_name + ".txt")
                fp = open(filepath, "wb")
                fp.close()

                greeting = "Welcome to Facegood, {}. I am Noone.".format(new_user.user_name)
                greet_msg = Message(current_app.config.get("GREETER"), str(uid), greeting)
                greet_msg.send_msg()

                flash('Registration Successful')
                return redirect('/login')
                # Create Pubkey File Name
                # Create Privkey File Name
                # Generate Keypair
            else:
                error = "User already exists."

    return render_template('forms/register.html', form=form, err=error)


