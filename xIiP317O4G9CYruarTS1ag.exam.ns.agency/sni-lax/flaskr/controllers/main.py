from flask import Blueprint, abort, render_template, request, current_app, flash, redirect, url_for, make_response
import json
import re

from flaskr.app import db
from flaskr.forms import LoginForm, ResetForm1, ResetForm2
from flaskr.models import User, Email

from base64 import b64encode, b64decode

from functools import wraps
from flask import g, flash, redirect, url_for
import hashlib

main = Blueprint('main', __name__)

USER = 'username'
ROLE = 'role'
SECRET = 'secret'
SESSION = 'session'


def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


def sha1(s):
    return hashlib.sha1(s.encode('utf-8')).hexdigest()


def b64_cookie(obj):
    data = json.dumps(obj)
    return b64encode(data.encode('utf-8'))


def sendmail(subject, body):
    e = Email(subject=subject, body=body)
    db.session.add(e)
    db.session.commit()


def admin_login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if not g.user.is_admin:
            return "Administrators Only", 403
        return f(*args, **kwargs)
    return wrap


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        try:

            if SESSION not in request.cookies:
                #flash('no session cookie')
                return redirect(url_for('.login'))
            cookie = request.cookies[SESSION]
            users = User.query.all()

            for u in users:
               if sha1(u.username) == cookie:
                   g.user = u
                   return f(*args, **kwargs)


            flash('invalid session cookie')
            return redirect(url_for('.login'))

        except Exception as e:
            return logout_user()

    return wrap


def login_user(u, form):

    cookie = sha1(u.username)


    #print(cookie)
    resp = make_response(redirect(url_for('.index')))
    resp.set_cookie(SESSION, cookie)
    return resp


def logout_user():
    resp = make_response(redirect(url_for('.login')))
    resp.set_cookie(SESSION, '')
    return resp


def password_reset(user, password):
    print("Setting password for '%s' to '%s'" % (user, password))
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('.login'))


@main.route('/robots.txt')
def robots():
    resp = current_app.make_response('''
User-agent: *
Disallow: /admin
''')
    resp.mimetype = "text/plain"
    return resp


@main.route('/reset', methods=['GET', 'POST'])
def reset_1():

    return abort(404)

    form = ResetForm1()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            flash('Invalid Username')
        else:
            pass


    return render_template('reset_1.html', title='Password Reset (1/2)', form=form)


@main.route('/reset/<uname>', methods=['GET', 'POST'])
def reset_2(uname):

    return abort(404)

    form = ResetForm2(username=uname)
    token = request.args.get('token') or ''
    check_user = User.query.filter_by(username=uname).first()
    if form.validate_on_submit():


        if check_user is None or reset_user is None:
            flash('Invalid Username')
        elif not check_user.check_reset(form.response.data, token):
            flash("Invalid Token")
        else:
            flash('Password Reset Successful')
            return password_reset(reset_user, form.password.data)

    return render_template('reset_2.html', title='Password Reset (2/2)', subtitle='Verify account ownership', form=form, q=check_user.reset_q)




@main.route('/login', methods=['GET', 'POST'])
def login():

    # redirect logged in users
    # if g.user and g.user.is_authenticated:
    #    return redirect(url_for('.index'))
    # return form

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            flash('Invalid Username')
        elif not user.check_password(form.password.data):
            flash('Invalid Password')
        else:
            return login_user(user, form)

    return render_template('login.html', title='GIBSON', form=form)


@main.route('/logout')
def logout():
    return logout_user()


@main.route('/')
@login_required
def index():
    return render_template('base.html', title="GIBSON", subtitle="Dashboard", flag='Well done! Get flag at /admin')


@main.route('/admin')
@login_required
@admin_login_required
def admin():
    return render_template('base.html', title="Congratulations!", subtitle="Super Secret Admin Panel", flag=current_app.config.get("FLAG"))

