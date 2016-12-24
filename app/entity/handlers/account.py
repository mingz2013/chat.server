# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from ..net.message_handler import msgHandler


@msgHandler.on("login")
def login(conn, data):
    print data
    pass
