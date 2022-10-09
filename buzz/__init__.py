import os
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE='database.db'
    )

    if test_config != None:
        app.config.from_mapping(test_config)
    else:
        app.config.from_pyfile('config.py')

    from . import db
    db.init_app(app)

    @app.route("/hello")
    def hello():
        return "hello world"
    
    @app.route("/")
    def index():
        return

    return app