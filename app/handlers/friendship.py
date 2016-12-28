# -*- coding:utf-8 -*-
__author__ = 'zhaojm'
from ..net.msg_handler import msgHandler
from ..dao.message import MessageDao


@msgHandler.on("friends_add")
def friends_add(conn, manager, data):
    print data
    try:
        if not data:
            raise Exception("data not found")
        send_to = data.get("username")
        send_from = conn.get_user().username
        print send_from
        send_to_conn = manager.getConnectionByUsername(send_to)
        if send_to_conn:
            send_to_conn.send({
                "cmd": "message",
                "data": {
                    "retcode": 0,
                    "result": {
                        "type": "friends_add",
                        "send_from": send_from,
                        "send_to": send_to,
                        "content": ""
                    }}})
        else:
            ret = MessageDao.message_add(type="friends_add", send_from=send_from, send_to=send_to)
            print ret
        conn.send({"cmd": "friends_add", "data": {"retcode": 0, "result": "success"}})
    except Exception, e:
        print e
        conn.send({"cmd": "friends_add", "data": {"retcode": -1, "errmsg": e.message}})


@msgHandler.on("friends_list")
def friends_list(conn, manager, data):
    print data
    pass


@msgHandler.on("friends_remove")
def friends_remove(conn, manager, data):
    print data
    pass
