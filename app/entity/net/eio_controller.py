# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from app import eio

from .ConnectionManager import ConnectionManager
from ..handler import service

connectionManager = ConnectionManager()


@eio.on('connect')
def connect(sid, environ):
    print("connect ", sid)

    connectionManager.addConnection(sid)


@eio.on('message')
def message(sid, message):
    print('message from', sid, message)
    print sid
    print type(message)
    # eio.send(sid, 'Thank you for your message!', binary=False)
    conn = connectionManager.getConnectionByID(sid)
    service.callTarget(conn, message)


@eio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)
    connectionManager.dropConnectionByID(sid)
