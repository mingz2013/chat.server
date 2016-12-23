# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from app import db
from BaseModel import BaseModel


class Room(BaseModel):
    creator = db.ObjectIdField()


class PrivateRoom(Room):
    # 私聊窗口
    friend = db.ObjectIdField()


class PublicRoom(Room):
    # 多聊窗口
    members = db.ObjectIdField()
