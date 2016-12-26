# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import json
from app.entity import io

from .msg_handler import msgHandler


@io.on('connect')
def connect(sid, environ):
    print "connect ", sid
    msgHandler.connManager.addConnection(sid)


@io.on('message')
def message(sid, message):
    print 'message from', sid, message
    msgHandler.handle_message(sid, message)


@io.on('disconnect')
def disconnect(sid):
    print 'disconnect ', sid
    msgHandler.connManager.dropConnection(sid)
