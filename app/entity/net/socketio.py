# -*- coding:utf-8 -*-
__author__ = 'zhaojm'


def create_socketio(app):
    # Set this variable to "threading", "eventlet" or "gevent" to test the
    # different async modes, or leave it set to None for the application to choose
    # the best option based on installed packages.
    # async_mode = None
    async_mode = "gevent"
    from flask_socketio import SocketIO
    socketio = SocketIO(app, async_mode=async_mode)

    from entity.net.ChatNamespace import ChatNamespace
    socketio.on_namespace(ChatNamespace('/chat'))

    return socketio
