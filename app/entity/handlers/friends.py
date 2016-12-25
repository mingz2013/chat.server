# -*- coding:utf-8 -*-
__author__ = 'zhaojm'
from ..net.message_handler import msgHandler


@msgHandler.on("friends_add")
def friends_add(conn, manager, data):
    print data
    pass


@msgHandler.on("friends_list")
def friends_list(conn, manager, data):
    print data
    pass


@msgHandler.on("friends_remove")
def friends_remove(conn, manager, data):
    print data
    pass
