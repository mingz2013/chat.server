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

from namespaces.ChatNamespace import ChatNamespace


class Application(object):
    def __init__(self):
        self.buffer = []

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO'].strip('/') or 'index.html'

        if path.startswith("socket.io"):
            socketio_manage(environ, {'/chat': ChatNamespace})
        else:
            return not_found(start_response)


def not_found(start_response):
    start_response('404 Not Found', [])
    return ['<h1>Not Found</h1>']
