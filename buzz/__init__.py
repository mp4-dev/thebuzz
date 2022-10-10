import os
from flask import Flask, request, redirect, render_template, flash
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
            err = None
            content = request.form['content']

            if not content:
                err = "Content cannot be empty!"

            if err is not None:
                flash(err)
            else:
                db.query_db("INSERT INTO posts (content) VALUES(?)", (content,))
                
            return redirect("/")
        else:
            posts = db.query_db("SELECT content FROM posts")
            return render_template('index.html', posts=posts)

    return app