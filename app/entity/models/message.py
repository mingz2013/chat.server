# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from app import db


class Message(db.Document):
    send_time = db.DateTimeField()
    content = db.StringField()
    send_from = db.ObjectIdField()

