#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask_wtf import Form, RecaptchaField
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, URL
from webapp.models import User

class CommentForm(Form):
    name = StringField('name', validators=[DataRequired(), Length(max=255)])
    text = TextAreaField(u'Comment', validators=[DataRequired()])

class LoginForm(Form):
    username = StringField('username', [DataRequired(), Length(max=255)])
    password = PasswordField('password', [DataRequired()])
    remember = BooleanField("Remember me")

    def validate(self):
        check_validate = super(LoginForm, self).validate()

        if not check_validate:
            return False

        user = User.query.filter_by(username=self.username.data).first()

        if not user:
            self.username.errors.append('Invalid username or password')
            return False

        if not user.check_password(self.password.data):
            self.username.errors.append('invalid username or password')
            return False

        return True

class RegisterForm(Form):
    username = StringField('Username', [DataRequired(), Length(max=255)])
    password = PasswordField('Password', [DataRequired(), Length(min=8)])
    confirm = PasswordField('Confirm Password', [DataRequired(), EqualTo('password')])

    def validate(self):
        check_validate = super(RegisterForm, self).validate()

        if not check_validate:
            return False

        user = User.query.filter_by(username=self.username.data).first()

        if user:
            self.username.errors.append("User with that name already exists")
            return False

        return True

class PostForm(Form):
    title = StringField('title', [DataRequired(), Length(max=255)])
    type = SelectField('Post Type', choices=[
        ('blog', 'Blog Post'),
        ('image', 'Image'),
        ('video', 'Video'),
        ('quote', 'Quote')
    ])
    text = TextAreaField('Content')
    image = StringField('Image URL', [URL(), Length(max=255)])
    video = StringField('Video Code', [Length(max=255)])
    author = StringField('Author', [Length(max=255)])

class OpenIDForm(Form):
    openid = StringField('OpenID URL', [DataRequired(), URL()])