# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from .Connection import Connection


# 每一个链接的管理器
class ConnectionManager(object):
    def __init__(self):
        self._connections = {}

    def getNowConnCnt(self):
        return len(self._connections.items())

    def addConnection(self, sid):

        _conn = Connection(sid)
        if self._connections.has_key(_conn.sid):
            raise Exception("系统记录冲突")
        self._connections[_conn.sid] = _conn

    def dropConnectionByID(self, sid):
        try:
            del self._connections[sid]
        except Exception as e:
            pass

    def getConnectionByID(self, sid):
        return self._connections.get(sid, None)
