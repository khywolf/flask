#!/usr/bin/env python
#-*- coding:utf-8 -*-
import smtplib
import datetime
from webapp.extensions import celery
from email.mime.text import MIMEText
from webapp.models import Reminder, Post

@celery.task()
def log(msg):
    return msg

@celery.task()
def multiply(x, y):
    return x * y

@celery.task(
    bind=True,
    ignore_result=True,
    default_retry_delay=300,
    max_retries=5
)

def remind(self, pk):
    reminder = Reminder.query.get(pk)
    msg = MIMEText(reminder.text)

    msg['Subject'] = "Your reminder"
    msg['From'] = Your_email
    msg['To'] = reminder.email

    try:
        smtp_server = smtplib.SMTP('localhost')
        smtp_server.starttls()
        smtp_server.login(user,password)
        smtp_server.sendmail(
            your_email,
            [reminder.email],
            msg.as_string()
        )
        smtp_server.close()

        return

    except Exception, e:
        self.retry(exc=e)

@celery.task(
    bind=True,
    ignore_result=True,
    default_retry_delay=300,
    max_retries=5
)
def digest(self):
    #找出这周的起始日和结束日
    year, week = datetime.datetime.now().isocalendar()[0:2]
    date = datetime.date(year, 1, 1)
    if (date.weekday() > 3):
        date = date + datetime.timedelta(days=7 - date.weekday())
    else:
        date = date - datetime.timedelta(days=date.weekday())
    delta = datetime.timedelta(days=(week - 1) * 7)
    start, end = date + delta, date + delta + datetime.timedelta(days=6)

    posts = Post.query.filter(
        Post.publish_date >= start,
        Post.publish_date <= end
    ).all()

    if (len(posts) == 0):
        return

    msg = MIMEText(
        render_template("digest.html", posts=posts), 'html'
    )

    msg['Subject'] = "Weekly Digest"
    msg['From'] = "your_email"

    try:
        smtp_server = smtplib.SMTP('localhost')
        smtp_server.starttls()
        smtp_server.login('user','password')
        smtp_server.sendmail(
            'your email',
            [recipients],
            msg.as_string()
        )
        smtp_server.close()

        return
    except Exception, e:
        self.retry(exc=e)

def on_reminder_save(mapper, connect, self):
        remind.apple_async(args=(self.id), eta=self.date)