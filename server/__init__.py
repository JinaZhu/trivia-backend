from flask import Flask
import os

from .api import api

def create_app():
    app = Flask(__name__)
    print("hello")

    app.register_blueprint(api)

    return app