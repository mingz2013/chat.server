# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from app import db


class User(db.Document):
    username = db.StringField(required=True)
    password = db.StringField(max_length=50)
