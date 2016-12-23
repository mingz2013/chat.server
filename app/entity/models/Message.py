# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from app import db
from BaseModel import BaseModel


class Message(BaseModel):
    send_time = db.DateTimeField()
    content = db.StringField()


class ChatMessage(Message):
    room = db.ObjectIdField()
    send_from = db.ObjectIdField()


class SystemMessage(Message):
    pass
