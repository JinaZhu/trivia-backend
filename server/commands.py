import click
from flask.cli import with_appcontext
from .extensions import db
from .model import Question
from .seed import load_sample_questions

@click.command(name="create_tables")
@with_appcontext
def create_tables():
    db.create_all()
    

@click.command(name="seed_questions")
@with_appcontext
def seed_questions():
    load_sample_questions()
    

@click.command(name="say_hi")
@with_appcontext
def say_hi():
    print('hi world')