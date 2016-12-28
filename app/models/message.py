# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from mongoengine import Document, ObjectIdField, DateTimeField, StringField


class Message(Document):
    send_time = DateTimeField()
    send_from = ObjectIdField()
    send_to = ObjectIdField()
    content = StringField()
    type = StringField()
