#!/usr/bin/env python
#-*- coding:utf-8 -*-
from flask import abort
from flask.ext.restful import Resource, fields, marshal_with
from webapp.models import Post, db, User, Tag
from .fields import HTMLField
from .parsers import post_get_parser

nested_tag_fields = {
    'id': fields.Integer(),
    'title': fields.String()
}

post_fields = {
    'title': fields.String(),
    'text': HTMLField(),
    'tags': fields.List(fields.Nested(nested_tag_fields)),
    'author': fields.String(attribute=lambda x: x.user_id),
    'publish_date': fields.DateTime(dt_format='iso8601')
}

class PostApi(Resource):
    @marshal_with(post_fields)
    def get(self, post_id=None):
        if post_id:
            post = Post.query.get(post_id)
            if not post:
                abort(404)
            return post
        else:
            args = post_get_parser.parse_args()
            page = args['page'] or 1

            if args['user']:
                user = User.query.filter_by(
                    username=args['user']
                ).first()
                if not user:
                    abort(404)

                posts = Post.query.order_by(
                    Post.publish_date.desc()
                ).paginate(page, 4)
            else:
                posts = Post.query.order_by(
                    Post.publish_date.desc()
                ).paginate(page, 2)

            return posts.items