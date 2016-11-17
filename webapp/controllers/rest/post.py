#!/usr/bin/env python
#-*- coding:utf-8 -*-
from flask import abort
from flask.ext.restful import Resource, fields, marshal_with

class PostApi(Resource):
    def get(self, post_id=None):
        if post_id:
            return {"id": post_id}
        return {'hello': 'world'}