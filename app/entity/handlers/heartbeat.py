# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from ..net.message_handler import msgHandler


@msgHandler.on("heartbeat")
def heartbeat(conn, manager, data):
    print data
    pass
