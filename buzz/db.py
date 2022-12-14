import sqlite3
import click
from flask import current_app, g

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(current_app.config['DATABASE'])
    db.row_factory = make_dicts
    return db


def close_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value) for idx, value in enumerate(row))

def query_db(query, args=(), one=False, reverse=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    get_db().commit()
    print("query success")
    return (rv[0] if rv else None) if one else rv

def init_db(e=None):
    with current_app.app_context():
        db = get_db()
        with current_app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@click.command('init-db')
def initialize_database():
    init_db()

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(initialize_database)