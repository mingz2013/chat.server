# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from app import db


class Message(db.Document):
    send_time = db.DateTimeField()
    send_from = db.ObjectIdField()
    send_to = db.ObjectIdField()
    content = db.StringField()
    type = db.StringField()
