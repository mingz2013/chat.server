# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from .packet import Packet


class BasePacket(Packet):
    def __init__(self, cmd, data):
        Packet.__init__(self, cmd, data)

    def send(self):
        pass

    def as_json(self):
        pass
