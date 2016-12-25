# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from ..net.message_handler import msgHandler


@msgHandler.on("user_find")
def user_find(conn, manager, data):
    print data
    pass


@msgHandler.on("user_list")
def user_list(conn, manager, data):
    print data
    pass


@msgHandler.on("user_info")
def user_info(conn, manager, data):
    print data
    pass
