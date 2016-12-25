# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from ..net.message_handler import msgHandler
from ..dao import UserDao


@msgHandler.on("register")
def register(conn, manager, data):
    print data
    try:
        if not data:
            raise Exception("data not found")
        username = data.get("username")
        password = data.get("password")
        UserDao.add_user(username, password)
        token = username + password
        auth = {"token": token}

        conn.send({"retcode": 0, "cmd": "register", "result": auth})
    except Exception, e:
        conn.send({"retcode": -1, "cmd": "register", "errmsg": e.message})


@msgHandler.on("login")
def login(conn, manager, data):
    print data
    try:
        if not data:
            raise Exception("data not found")
        username = data.get("username")
        password = data.get("password")
        ret = UserDao.check_login(username, password)
        if not ret:
            raise Exception("not auth pass..")
        else:
            token = username + password
            auth = {"token": token}
            conn.send({"retcode": 0, "cmd": "register", "result": auth})
    except Exception, e:
        conn.send({"retcode": -1, "cmd": "login", "errmsg": e.message})


@msgHandler.on("account_info")
def account_info(conn, manager, data):
    pass
