# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from app import db
from BaseModel import BaseModel


class User(BaseModel):
    username = db.StringField(required=True)
    password = db.StringField(max_length=50)
