#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask.ext.bcrypt import Bcrypt
from flask.ext.openid import OpenID
from flask.ext.login import LoginManager
from flask.ext.restful import Api
from flask.ext.principal import Principal, Permission, RoleNeed

bcrypt = Bcrypt()
oid = OpenID()
login_manager = LoginManager()
principals = Principal()
rest_api = Api()

admin_permission = Permission(RoleNeed('admin'))
poster_permission = Permission(RoleNeed('poster'))
default_permission = Permission(RoleNeed('default'))

login_manager.login_view = "main.login"
login_manager.session_protection = "strong"
login_manager.login_message = "Please login to access this page"
login_manager.login_category = "info"

@login_manager.user_loader
def load_user(userid):
    from models import User
    return User.query.get(userid)

@oid.after_login
def create_or_login(resp):
    from models import db, User
    username = resp.fullname or resp.nickname or resp.email
    if not username:
        flash('Invalid login. Please try again', 'danger')
        return redirect(url_for('main.login'))

    user = User.query.filter_by(username=username).first()
    if user is None:
        user = User(username)
        db.session.add(user)
        db.session.commit()

    return redirect(url_for('blog.main'))
