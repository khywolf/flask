#!/usr/bin/env python
#-*- coding:utf-8 -*-
from flask.ext.restful import reqparse

post_get_parser = reqparse.RequestParser()
post_get_parser.add_argument(
    'page',
    type=int,
    location=['args', 'headers']
)
post_get_parser.add_argument(
    'user',
    type=str,
    location=['args', 'headers']
)