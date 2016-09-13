#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length

class CommentForm(Form):
    name = StringField('name', validators=[DataRequired(), Length(max=255)])
    text = TextAreaField(u'Comment', validators=[DataRequired()])