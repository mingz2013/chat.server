# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from app import eio


@eio.on('connect')
def connect(sid, environ):
    print("connect ", sid)


@eio.on('message')
def message(sid, data):
    print('message from', sid, data)
    eio.send(sid, 'Thank you for your message!', binary=False)


@eio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)
