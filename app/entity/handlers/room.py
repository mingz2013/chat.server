# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from ..net.message_handler import msgHandler


@msgHandler.on("room_create")
def room_create(conn, manager, data):
    pass


@msgHandler.on("room_invite")
def room_invite(conn, manager, data):
    pass


@msgHandler.on("room_drop")
def room_drop(conn, manager, data):
    pass


@msgHandler.on("room_list")
def room_list(conn, manager, data):
    pass


@msgHandler.on("room_add")
def room_add(conn, manager, data):
    pass


@msgHandler.on("room_info")
def room_info(conn, manager, data):
    pass


@msgHandler.on("room_quit")
def room_quit(conn, manager, data):
    pass
