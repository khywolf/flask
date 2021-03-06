#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand
from webapp import create_app
from webapp.models import db, User, Post, Comment, BlogPost, VideoPost, ImagePost, QuotePost, Reminder

env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app('webapp.config.%sConfig' % env.capitalize())

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command("server", Server(host='0.0.0.0'))
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post, Comment=Comment, BlogPost=BlogPost, VideoPost=VideoPost, ImagePost=ImagePost, QuotePost=QuotePost, Reminder=Reminder)

@manager.command
def test():
    print "Hello World!"

if __name__ == "__main__":
    manager.run()
