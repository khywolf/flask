#!/usr/bin/env python
#-*- coding:utf-8 -*-
import datetime

class Config(object):
    SECRET_KEY = 'key here'
    RECAPTCHA_PUBLIC_KEY = '6LeIByoTAAAAABLjathhgXR6lrcw25Yhmi7Ki7bK'
    RECAPTCHA_PRIVATE_KEY = '6LeIByoTAAAAAEVV9B3WfLN0qhdQGZqUsxYOz6eg'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@172.16.1.129:3306/flask"
    AQLALCHEMY_ECHO = True
    SECRET_KEY = '743acb049b060a523d2fbf6155c2043d'
    MONGODB_SETTINGS = {
        'db': 'local',
        'host': '172.16.1.129',
        'port': 27017
    }
    CELERY_BROKER_URL = "redis://172.16.1.129:6379/0"
    CELERY_RESULT_BACKEND = "redis://172.16.1.129:6379/1"
    CELERYBEAT_SCHEDULE = {
        'log-every-5-seconds': {
            'task': 'webapp.tasks.log',
            'schedule': datetime.timedelta(seconds=5),
            'args': ("Message schedule",)
        },
    }