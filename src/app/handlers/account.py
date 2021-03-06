# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from ..net.msg_handler import msg_handler
from ..dao import UserDao


@msg_handler.on("register")
def register(conn, manager, data):
    print data
    try:
        if not data:
            raise Exception("data not found")
        username = data.get("username")
        password = data.get("password")
        user = UserDao.find_user_by_username(username)
        if user:
            raise Exception("username is exists already")
        UserDao.add_user(username, password)
        token = username + password
        auth = {"token": token}

        conn.send({"cmd": "register", "data": {"retcode": 0, "result": auth}})
    except Exception, e:
        conn.send({"cmd": "register", "data": {"retcode": -1, "errmsg": e.message}})


@msg_handler.on("login")
def login(conn, manager, data):
    print data
    try:
        if not data:
            raise Exception("data not found")
        username = data.get("username")
        password = data.get("password")
        user = UserDao.check_login(username, password)
        if not user:
            raise Exception("not auth pass..")
        else:
            conn.set_user(user)
            token = username + password
            auth = {"token": token}
            conn.send({"cmd": "login", "data": {"retcode": 0, "result": auth}})
    except Exception, e:
        conn.send({"cmd": "login", "data": {"retcode": -1, "errmsg": e.message}})


@msg_handler.on("account_info")
def account_info(conn, manager, data):
    pass
