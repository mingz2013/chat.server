# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from .connection import Connection


class ConnectionManager(object):
    def __init__(self):
        self._connections = {}
        pass

    def add_connection(self, sid):
        _conn = Connection(sid)
        if self._connections.has_key(sid):
            raise Exception("add a connection already had")
        self._connections[sid] = _conn

    def drop_connection(self, sid):
        try:
            del self._connections[sid]
        except Exception, e:
            print e

    def get_connection(self, sid):
        return self._connections.get(sid)

    def disconnect(self, sid):
        """根据连接ID主动断开与客户端的连接"""
        _conn = self.get_connection(sid)
        if _conn:
            _conn.disconnect()
            self.drop_connection(sid)

    def send(self, msg, receivers):
        """主动推送消息"""
        assert isinstance(receivers, list), "receivers type error"
        for sid in receivers:
            try:
                _conn = self.get_connection(sid)
                if _conn:
                    _conn.send(msg)
            except Exception, e:
                print e

    def get_connection_by_username(self, username):
        for (sid, conn) in self._connections.items():
            user = conn.user
            if user.username == username:
                return conn
