# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from mongoengine import Document, StringField


class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
