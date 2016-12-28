# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from mongoengine import Document, ObjectIdField, DateTimeField, StringField


class Room(Document):
    creator = ObjectIdField()


class PrivateRoom(Room):
    # 私聊窗口
    friend = ObjectIdField()


class PublicRoom(Room):
    # 多聊窗口
    members = ObjectIdField()
