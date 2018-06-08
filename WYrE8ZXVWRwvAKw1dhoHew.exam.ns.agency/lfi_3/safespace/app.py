from flask import Flask

from safespace.controllers.main import main
from datetime import datetime, timedelta
import os
import re

app = Flask(__name__)

def register_blueprints(app):
    app.register_blueprint(main)

def create_app():
    global app
    register_blueprints(app)
    return app
