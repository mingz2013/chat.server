# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from app.entity import eio


# 每一个链接
class Connection(object):
    def __init__(self, sid):
        self.sid = sid
        self.user = None
        pass

    def send(self, data, binary=False):
        eio.send(self.sid, data, binary=binary)

    def disconnect(self):
        eio.disconnect(self.sid)
        pass

    def set_user(self, user):
        self.user = user

    def get_user(self):
        return self.user
