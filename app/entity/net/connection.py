# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from app.entity import io


# 每一个链接
class Connection(object):
    def __init__(self, sid):
        self.sid = sid
        self.user = None
        pass

    def send(self, data, binary=None, callback=None):
        print "send, ", data
        io.send(room=self.sid, data=data, binary=binary, callback=callback)

    def disconnect(self):
        io.disconnect(self.sid)
        pass

    def set_user(self, user):
        self.user = user

    def get_user(self):
        return self.user
