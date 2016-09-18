#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, redirect, url_for
from config import DevConfig

from models import db
from controllers.blog import blog_blueprint
from webapp.extensions import bcrypt

def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(DevConfig)
    db.init_app(app)
    bcrypt.init_app(app)

    @app.route('/')
    def index():
        return redirect(url_for('blog.home'))

    app.register_blueprint(blog_blueprint)

    return app

if __name__ == '__main__':
    app.run()