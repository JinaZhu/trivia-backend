import click
from flask.cli import with_appcontext
from .extensions import db
from .model import Question

@click.command(name="create_tables")
@with_appcontext
def create_tables():
    db.create_all()
    print('db', db)
    print("tables created")

@click.command(name="say_hi")
@with_appcontext
def say_hi():
    print('hi world')