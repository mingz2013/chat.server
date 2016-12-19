# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

if __name__ == '__main__':
    from geventwebsocket import WebSocketServer, WebSocketApplication, Resource
    from ChatApplication import ChatApplication

    WebSocketServer(
        ('', 9000),
        Resource({'/chat': ChatApplication})
    ).serve_forever()
