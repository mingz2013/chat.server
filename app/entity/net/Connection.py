# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from app import eio


# 每一个链接
class Connection(object):
    def __init__(self, sid):
        self.sid = sid
        pass

    def send(self, data, binary=False):
        eio.send(self.sid, data, binary=binary)
