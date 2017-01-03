#!/usr/bin/env python
#-*- coding:utf-8 -*-
from flask.ext.admin import BaseView, expose
from flask.ext.admin.contrib.sqla import ModelView

class CustomView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/custom.html')

    @expose('/second_page')
    def second_page(self):
        return self.render('admin/second_page.html')

class CustomModelView(ModelView):
    pass