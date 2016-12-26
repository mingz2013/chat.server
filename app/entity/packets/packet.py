# -*- coding:utf-8 -*-
__author__ = 'zhaojm'


class Packet(object):
    def __init__(self, cmd, data):
        self.cmd = cmd
        self.data = data
        pass
