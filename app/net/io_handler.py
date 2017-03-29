# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import json
from .. import io

from .msg_handler import msg_handler


@io.on('connect')
def connect(sid, environ):
    print "connect ", sid
    msg_handler.conn_manager.add_connection(sid)


@io.on('message')
def message(sid, message):
    print 'message from', sid, message
    msg_handler.handle_message(sid, message)


@io.on('disconnect')
def disconnect(sid):
    print 'disconnect ', sid
    msg_handler.conn_manager.drop_connection(sid)
