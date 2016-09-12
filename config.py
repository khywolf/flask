#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@172.16.1.129:3306/flask"
    AQLALCHEMY_ECHO = True
    SECRET_KEY = '743acb049b060a523d2fbf6155c2043d'