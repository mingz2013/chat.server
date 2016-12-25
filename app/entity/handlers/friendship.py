# -*- coding:utf-8 -*-
__author__ = 'zhaojm'
from ..net.message_handler import msgHandler


@msgHandler.on("friend_add")
def friend_add(conn, manager, data):
    print data
    pass


@msgHandler.on("friend_list")
def friend_list(conn, manager, data):
    print data
    pass


@msgHandler.on("friend_remove")
def friend_remove(conn, manager, data):
    print data
    pass
