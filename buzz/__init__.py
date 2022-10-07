import os
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config != None:
        app.config.from_mapping(test_config)
    else:
        app.config.from_pyfile('config.py')
    
    @app.route("/hello")
    def hello():
        return "hello world"
    
    return app