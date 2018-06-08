from flask import Blueprint, render_template, request, render_template_string, current_app, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from multiprocessing import Process
from datetime import datetime
from dateutil import tz
import re
import json
from datetime import datetime

from . import horseman

from flaskr.app import db
from flaskr.forms import LoginForm, RegistrationForm, TrashForm, highlighters
from flaskr.models import User, Trash, default_uuid, default_trash_index

main = Blueprint('main', __name__)


@main.errorhandler(404)
def page_not_found(error):
    return '404 page not found', 404


@main.route('/robots.txt')
def robots():
    resp = current_app.make_response('''
User-agent: *
Disallow: /?
''')
    resp.mimetype = "text/plain"
    return resp


@main.route('/home')
@login_required
def home():
    title = '''
    YOUR OWN LITTLE DUMPSTER
    <svg class="icon" xmlns="http://www.w3.org/2000/svg" width="12" height="16" viewBox="0 0 12 16">
        <path fill-rule="evenodd" d="M5.05.01c.81 2.17.41 3.38-.52 4.31C3.55 5.37 1.98 6.15.9 7.68c-1.45 2.05-1.7 6.53 3.53 7.7-2.2-1.16-2.67-4.52-.3-6.61-.61 2.03.53 3.33 1.94 2.86 1.39-.47 2.3.53 2.27 1.67-.02.78-.31 1.44-1.13 1.81 3.42-.59 4.78-3.42 4.78-5.56 0-2.84-2.53-3.22-1.25-5.61-1.52.13-2.03 1.13-1.89 2.75.09 1.08-1.02 1.8-1.86 1.33-.67-.41-.66-1.19-.06-1.78C8.18 5.01 8.68 2.15 5.05.02L5.03 0l.02.01z"/>
    </svg>
    '''
    return render_template('home.html', title=title, trash=current_user.trash)


@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('.login'))
    return render_template('register.html', title='NEW USER', form=form)


@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('.home')
        return redirect(next_page)
    return render_template('login.html', title='SIGN IN', form=form)


@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('.index'))


@main.route('/')
def index():
    trash = Trash.query.filter_by(is_public=True).order_by(Trash.timestamp.desc()).all()
    return render_template('index.html', trash=trash, title="Recent Trash")


@main.route('/post', methods=['GET', 'POST'])
def trash_post():
    form = TrashForm()


    if form.validate_on_submit():
        user = current_user
        if user.is_anonymous:
            user = None
            uid = 'null'
        else:
            uid = user.id
        public = form.visibility.data == 'public'
        print(repr(form.content.data))

        trash = Trash(author=user, title=form.title.data, content=form.content.data,
                      highlight=form.highlight.data, is_public=public, password=form.password.data or '')
        db.session.add(trash)
        db.session.commit()
        tid = trash.uuid

        target_url = url_for(".trash_page", id=tid) + '?p=' + (form.password.data or '')


        return redirect(target_url)

    if request.method == "POST":
        flash("Invalid form submission")
        redirect(url_for(".index"))

    return render_template('post.html', form=form, title="GIVE US YOUR TRASH", subtitle="We'll glue it to the internet for you!")


def trash_from_row(row):
    t = Trash()
    t.uuid = row[0]
    t.idx = row[1]
    t.views = row[2]
    t.title = row[3]
    t.content = row[4]
    t.highlight = row[5]
    t.password = row[6]
    t.is_public = row[7]
    t.timestamp = row[8]
    t.user_id = row[9]
    return t


def trash_sql(s):
    try:
        result = db.engine.execute(s)
        for row in result:
            print(repr(row))
            return trash_from_row(row), None
        return None, None
    except Exception as e:
        print("*** ERROR ***")
        print(repr(e))
        return None, e


@main.route('/page/<id>')
def trash_page(id):

    tid = str(id)

    t, e = trash_sql("select * from trash where uuid='%s'" % sql_5(tid))
    if e is not None:
        flash(repr(e))
        return redirect(url_for(".index"))


    if t is None:
        return redirect(url_for('.index'))

    password = request.args.get('p') or ''
    check_pass = t.password or ''


    if password != check_pass:
        return render_template('base.html', title='Trash Protected', subtitle='Password Check Failed')

    t.views = t.views + 1
    db.session.commit()

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    utc = datetime.utcnow()
    utc = utc.replace(tzinfo=from_zone)
    t.timestamp = utc.astimezone(to_zone)

    return render_template('trash.html', trash=t, title="TRASH #%d" % t.idx, subtitle="One person's trash is another person's private key.", highlighters=highlighters)


def sql_filter(input, pattern, case_sensitive):
    if case_sensitive:
        return input.replace(pattern, '')
    else:
        regex = re.compile(pattern, re.IGNORECASE)
        return regex.sub('', input)


def sql_1(s):
    s = sql_filter(s, ' ', True)
    s = sql_filter(s, '%20', True)
    return s


def sql_2(s):
    s = s.replace("'", r"\'")
    return s


def sql_3(s):
    s = sql_filter(s, 'select', True)
    s = sql_filter(s, 'SELECT', True)
    s = sql_filter(s, 'from', True)
    s = sql_filter(s, 'FROM', True)
    s = sql_filter(s, 'union', True)
    s = sql_filter(s, 'UNION', True)
    s = sql_filter(s, 'flag', True)
    s = sql_filter(s, 'FLAG', True)
    s = sql_filter(s, 'or', True)
    s = sql_filter(s, 'OR', True)
    s = sql_filter(s, 'limit', True)
    s = sql_filter(s, 'LIMIT', True)
    return s


def sql_4(s):
    s = s.replace("'", "''")
    s = s.replace('\\', '\\\\')
    return s


def sql_5(s):
    s = ''.join(c for c in s if c in "0x123456789abcdef\"'!@#$%^&*()_-+={}[]?<>.:;|~`/\\")
    return s

