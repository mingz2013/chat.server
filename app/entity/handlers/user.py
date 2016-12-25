# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from ..net.message_handler import msgHandler
from ..dao.user import UserDao

@msgHandler.on("user_find")
def user_find(conn, manager, data):
    print data
    pass


@msgHandler.on("user_list")
def get_user_list(conn, manager, data):
    print data
    try:
        user_list = UserDao.get_user_list()
        conn.send({"cmd": "user_list", "data": {"retcode": 0, "result": user_list}})
    except Exception, e:
        conn.send({"cmd": "user_list", "data": {"retcode": -1, "errmsg": e.message}})


@msgHandler.on("user_info")
def user_info(conn, manager, data):
    print data
    pass
