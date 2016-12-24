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
        return self._connections.get(sid)

    def disconnect(self, sid):
        """根据连接ID主动断开与客户端的连接
        """
        _conn = self.getConnection(sid)
        if _conn:
            _conn.disconnect()
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
