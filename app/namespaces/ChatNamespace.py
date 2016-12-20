# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from gevent import monkey

monkey.patch_all()
import gevent
# import psutil

from socketio import socketio_manage
from socketio.server import SocketIOServer
from socketio.namespace import BaseNamespace
from socketio.mixins import BroadcastMixin


class ChatNamespace(BaseNamespace):
    def recv_connect(self):
        def sendcpu():
            self.emit('cpu_data', {'point': 1})
            gevent.sleep(0.1)

        self.spawn(sendcpu)
