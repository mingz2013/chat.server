# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from mongoengine import Document, ObjectIdField, DateTimeField, StringField


class Message(Document):
    send_time = DateTimeField()
    send_from = StringField()
    send_to = StringField()
    content = StringField()
    type = StringField()
