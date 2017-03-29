# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from ..net.msg_handler import msg_handler


@msg_handler.on("send_message")
def send_message(conn, manager, data):
    print data
    pass


@msg_handler.on("request_message")
def request_message(conn, manager, data):
    print data
    pass
