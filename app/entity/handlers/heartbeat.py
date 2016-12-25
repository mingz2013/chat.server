# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from ..net.message_handler import msgHandler
from ..dao.message import MessageDao


@msgHandler.on("heartbeat")
def heartbeat(conn, manager, data):
    print data
    try:
        messages = MessageDao.get_messages_for_user(conn.get_user())
        conn.send({"cmd": "heartbeat", "data": {"retcode": 0, "result": messages}})
    except Exception, e:
        conn.send({"cmd": "heartbeat", "data": {"retcode": -1, "errmsg": e.message}})
