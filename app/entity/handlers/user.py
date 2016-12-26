# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from ..net.msg_handler import msgHandler
from ..dao.user import UserDao
from ..core.utils import model2dict


@msgHandler.on("user_find")
def user_find(conn, manager, data):
    print data
    pass


@msgHandler.on("user_list")
def get_user_list(conn, manager, data):
    print data
    try:
        user_list = UserDao.get_user_list()
        user_list_copy = []
        for user in user_list:
            user_copy = {
                "username": user.username
            }
            user_list_copy.append(user_copy)
        print user_list_copy
        conn.send({"cmd": "user_list", "data": {"retcode": 0, "result": user_list_copy}})
    except Exception, e:
        conn.send({"cmd": "user_list", "data": {"retcode": -1, "errmsg": e.message}})


@msgHandler.on("user_info")
def user_info(conn, manager, data):
    print data
    try:
        username = data.get("username")
        user = UserDao.find_user_by_username(username)
        user_copy = {
            "username": user.username
        }
        conn.send({"cmd": "user_info", "data": {"retcode": 0, "result": user_copy}})
    except Exception, e:
        conn.send({"cmd": "user_info", "data": {"retcode": -1, "errmsg": e.message}})
