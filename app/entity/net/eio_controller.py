# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from app.entity import eio

from .message_handler import msgHandler


@eio.on('connect')
def connect(sid, environ):
    print("connect ", sid)
    msgHandler.connManager.addConnection(sid)


@eio.on('message')
def message(sid, message):
    print('message from', sid, message)
    # eio.send(sid, 'Thank you for your message!', binary=False)
    msgHandler.handle_message(sid, message)


@eio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)
    msgHandler.connManager.dropConnection(sid)
