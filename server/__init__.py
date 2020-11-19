from flask import Flask
import os

from .api import api
from .commands import say_hi

def create_app():
    app = Flask(__name__)
    print("hello")

    app.register_blueprint(api)

    app.cli.add_command(say_hi)

    return app