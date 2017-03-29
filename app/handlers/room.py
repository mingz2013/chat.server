# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from ..net.msg_handler import msg_handler


@msg_handler.on("room_create")
def room_create(conn, manager, data):
    pass


@msg_handler.on("room_invite")
def room_invite(conn, manager, data):
    pass


@msg_handler.on("room_drop")
def room_drop(conn, manager, data):
    pass


@msg_handler.on("room_list")
def room_list(conn, manager, data):
    pass


@msg_handler.on("room_add")
def room_add(conn, manager, data):
    pass


@msg_handler.on("room_info")
def room_info(conn, manager, data):
    pass


@msg_handler.on("room_quit")
def room_quit(conn, manager, data):
    pass
