import os
from flask import Flask, request, redirect, render_template
from . import db

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

    db.init_app(app)

    @app.route("/hello")
    def hello():
        return "hello world"
    
    @app.route("/",methods=['POST','GET'])
    def index():
        if request.method == 'POST':
            content = request.form['content']
            db.query_db("INSERT INTO posts VALUES(?)", (content))
            return redirect("/")
        else:
            posts = db.query_db("SELECT * FROM posts")
            return render_template(posts=posts)

    return app