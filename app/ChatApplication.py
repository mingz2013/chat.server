# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import json

from geventwebsocket import WebSocketApplication


class ChatApplication(WebSocketApplication):
    def on_open(self):
        print "Connection opened"

    def on_message(self, message):
        obj = json.loads(message.decode('utf8'))
        print obj
        message = json.dumps(obj, ensure_ascii=False).encode('utf8')
        self.ws.send(message)

    def on_close(self, reason):
        print reason
