from flask import Flask
import os

from .extensions import db
from .api import api
from .commands import say_hi, create_tables

def create_app(config_file="settings.py"):
    app = Flask(__name__)
    print("hello")

    app.config.from_pyfile(config_file)
    db.init_app(app)

    app.register_blueprint(api)

    app.cli.add_command(say_hi)
    app.cli.add_command(create_tables)

    return app