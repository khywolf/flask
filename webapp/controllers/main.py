#!/usr/bin/env python
#-*- coding:utf-8 -*-
from flask import render_template, Blueprint, current_app, redirect, url_for, request, flash, session
from webapp.forms import LoginForm, RegisterForm, OpenIDForm
from webapp.models import db, Post, Comment, User
from webapp.extensions import oid
from flask.ext.login import login_user, logout_user
from flask.ext.login import login_required
from flask.ext.principal import (
    Identity,
    AnonymousIdentity,
    identity_changed
)

main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='../templates/main'
)

@main_blueprint.route('/')
def index():
    return redirect(url_for('blog.main'))

@main_blueprint.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    form = LoginForm()
    openid_form = OpenIDForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one()
        login_user(user, remember=form.remember.data)

        identity_changed.send(
            current_app._get_current_object(),
            identity=Identity(user.id)
        )

        flash("You have been logged in.", category="success")
        return redirect(url_for('blog.user', username=form.username.data))

    return render_template('login.html', form=form, openid_form=openid_form)

@main_blueprint.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    identity_changed.send(
        current_app._get_current_object(),
        identity=AnonymousIdentity()
    )
    flash("You have been logged out.", category="success")
    return redirect(url_for('.login'))

@main_blueprint.route('/register', methods=['GET', 'POST'])
@oid.loginhandler
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        new_user = User(form.username.data)
        new_user.set_password(form.password.data)

        db.session.add(new_user)
        db.session.commit()

        flash("Your user has been created, please login.", category="success")
        return redirect(url_for('.login'))

    return render_template('register.html', form=form)