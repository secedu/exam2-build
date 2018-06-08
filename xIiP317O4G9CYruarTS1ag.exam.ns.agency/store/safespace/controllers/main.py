from flask import Blueprint, render_template, request, render_template_string, current_app, flash, redirect, url_for, make_response, send_file
import os
import io
import subprocess
from time import sleep
import re
main = Blueprint('main', __name__)

SAFE_SPACE = os.getcwd() + '/safespace/safe'

def sym_sub(line):
    line = line.replace('/', '')
    line = line.replace('..', '')
    line = line.replace('%%2F', '')
    line = line.replace('%%2f', '')
    return line

@main.errorhandler(404)
def page_not_found(error):
    return '404 page not found', 404

@main.route('/robots.txt')
def robots():
    robots = 'User-agent: *\n'
    robots += 'Disallow: '

    robots += '/API/ping'


    resp = current_app.make_response(robots)
    resp.mimetype = "text/plain"
    return resp

@main.route('/')
def home():
    return render_template('pages/index.html')

@main.route('/about')
def about():
    return render_template('pages/about.html')

full_fpath = '../safe/'

@main.route('/safe/page')
def safe_page():
    if 'p' in request.args:
        try:
            name, ext = request.args['p'].split('.')
        except:
            return '404 page not found (Bad Input)', 404

        safe_pages = ['html']
        if ext not in safe_pages:
            return '404 page not found', 404
        else:
            full_fname = sym_sub(name + '.' + ext)

    else:
        return '404 page not found ("p" Empty)', 404

    safe_path = SAFE_SPACE + '/page/' + full_fname

    print("Safe Path: {}".format(safe_path))
    try:
        fp = open(safe_path, 'r')
    except:
        return '404 page not found (File Not Found)', 404

    file_content = fp.readlines()
    resp = render_template('pages/safe-space.html', lines=file_content)

    return resp


@main.route('/safe/doc')
def safe_doc():
    full_fname = None

    if 'd' in request.args:
        try:
            name, ext = request.args['d'].split('.')
        except:
            return '404 page not found (Bad Input)', 404
        safe_docs = ['md', 'txt']
        if ext not in safe_docs:
            return '404 page not found', 404
        else:
            full_fname = sym_sub(name + '.' + ext)
    else:
        return '404 page not found ("p" Empty)', 404

    safe_path = SAFE_SPACE + '/doc/' + full_fname

    print("Safe Path: {}".format(safe_path))
    try:
        fp = open(safe_path, 'r')
    except:
        return '404 page not found (File Not Found)', 404

    resp = make_response('\n'.join(fp.readlines()))
    resp.mimetype = 'text/plain'

    return resp

@main.route('/API/ping')
def ping():
    target = None
    if 'v' in request.args:
        target = request.args['v']
    else:
        return '404 page not found ("v" Empty)', 404

    p = subprocess.Popen(['/bin/sh'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate(bytes('ping -c 1 "{}"'.format(target), 'utf-8'), timeout=5)


    return out

@main.route('/safe/img')
def safe_img():

    full_fname = None
    ext = None # Default
    if 'i' in request.args:
        base = os.path.basename(sym_sub(request.args['i']))
        name, ext = os.path.splitext(base)
        safe_images = ['png', 'jpg']
        if ext.lstrip('.') not in safe_images:
            return '404 page not found', 404
        else:
            full_fname = name + ext
    else:
        return '404 page not found ("p" Empty)', 404

    safe_path = SAFE_SPACE + '/img/' + full_fname

    print("Safe Path: {}".format(safe_path))
    try:
        fp = open(safe_path, 'rb')
    except:
        return '404 page not found (File Not Found)', 404

    resp = send_file(io.BytesIO(fp.read()), mimetype='image/' + ext.lstrip('.'))
    return resp

