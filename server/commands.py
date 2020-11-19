import click
from flask.cli import with_appcontext

@click.command(name="say_hi")
@with_appcontext
def say_hi():
    print('hi world')