# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from ..net.msg_handler import msgHandler


@msgHandler.on("send_message")
def send_message(conn, manager, data):
    print data
    pass


@msgHandler.on("request_message")
def request_message(conn, manager, data):
    print data
    pass
