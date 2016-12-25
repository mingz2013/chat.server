# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from mongoengine import Document, ObjectIdField, DateTimeField, StringField


class User(Document):
    username = StringField(required=True)
    password = StringField(max_length=50)
