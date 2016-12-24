# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from .connection import Connection


class ConnectionManager(object):
    def __init__(self):
        self._connections = {}
        pass

    def addConnection(self, sid):
        _conn = Connection(sid)
        if self._connections.has_key(sid):
            raise Exception("系统记录冲突")
        self._connections[sid] = _conn

    def dropConnection(self, sid):
        try:
            del self._connections[sid]
        except Exception as e:
            print e

    def getConnection(self, sid):
        """根据ID获取一条连接
        @param connID: int 连接的id
        """
        return self._connections.get(sid)

    def loseConnection(self, sid):
        """根据连接ID主动端口与客户端的连接
        """
        _conn = self.getConnection(sid)
        if _conn:
            _conn.loseConnection()
            self.dropConnection(sid)

    def send(self, msg, receivers):
        """主动推送消息
        """
        assert isinstance(receivers, list), "receivers type error"
        for target in receivers:
            try:
                _conn = self.getConnection(target)
                if _conn:
                    _conn.send(msg)
            except Exception, e:
                print e
