#!/usr/bin/env python
#-*- coding:utf-8 -*-
from webapp.extensions import celery

@celery.task()
def log(msg):
    return msg

@celery.task()
def multiply(x, y):
    return x * y