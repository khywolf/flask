#!/usr/bin/env python
#-*- coding:utf-8 -*-

import random
import datetime
from main import app, db, User, Post, Comment, Tag
user = User.query.get(1)
tag_one = Tag('Python')
tag_two = Tag('Flask')
tag_three = Tag('SQLAlechemy')
tag_four = Tag('Jinja')
tag_list = [tag_one, tag_two, tag_three, tag_four]

s = "Example text"

for i in xrange(100):
    new_post = Post("port " + str(i))
    new_post.user = user
    new_post.publish_date = datetime.datetime.now()
    new_post.text = s
    new_post.tags = random.sample(tag_list, random.randint(1, 3))
    db.session.add(new_post)

db.session.commit()