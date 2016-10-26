#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, redirect, url_for
from config import DevConfig
from flask.ext.login import current_user
from flask.ext.principal import identity_loaded, UserNeed, RoleNeed

from models import db
from controllers.blog import blog_blueprint
from controllers.main import main_blueprint
from webapp.extensions import bcrypt, oid, login_manager, principals

def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)

    db.init_app(app)
    bcrypt.init_app(app)
    oid.init_app(app)
    login_manager.init_app(app)
    principals.init_app(app)

    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        #Set the identity user object
        identity.user = current_user

        #Add the UserNeed to the identity
        if hasattr(current_user, 'id'):
            identity.provides.add(UserNeed(current_user.id))

        #Add each role to the identity
        if hasattr(current_user, 'roles'):
            for role in current_user.roles:
                identity.provides.add(RoleNeed(role.name))

    @app.route('/')
    def index():
        return redirect(url_for('blog.home'))

    app.register_blueprint(blog_blueprint)
    app.register_blueprint(main_blueprint)

    return app

if __name__ == '__main__':
    app.run()