#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand
from webapp import create_app
from webapp.models import db, User, Post, Comment, Tag, Userm, Commentm, Postm, BlogPost, VideoPost, ImagePost, QuotePost

env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app('webapp.config.%sConfig' % env.capitalize())

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command("server", Server(host='0.0.0.0'))
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post, Comment=Comment, Tag=Tag, Userm=Userm, Commentm=Commentm, Postm=Postm, BlogPost=BlogPost, VideoPost=VideoPost, ImagePost=ImagePost, QuotePost=QuotePost)

if __name__ == "__main__":
    manager.run()
