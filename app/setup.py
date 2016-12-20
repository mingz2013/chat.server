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

if __name__ == '__main__':
    print 'Listening on port http://0.0.0.0:8080 and on port 10843 (flash policy server)'
    SocketIOServer(('0.0.0.0', 9000), Application(),
                   resource="socket.io", policy_server=True,
                   policy_listener=('0.0.0.0', 10843)).serve_forever()
