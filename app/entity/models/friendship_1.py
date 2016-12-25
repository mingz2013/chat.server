# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from app import db


class Friendship(db.Document):
    user = db.ObjectIdField()
    friend = db.ObjectIdField()
