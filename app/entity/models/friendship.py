# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from mongoengine import Document, ObjectIdField


class Friendship(Document):
    user = ObjectIdField()
    friend = ObjectIdField()
