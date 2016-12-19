# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import json
from ChatWSServerProtocol import ChatWSServerProtocol

from autobahn.twisted.resource import WebSocketResource
from autobahn.twisted.websocket import WebSocketServerFactory


def create_chat_ws_resource():
    # create a Twisted Web resource for our WebSocket server
    wsFactory = WebSocketServerFactory(u"ws://127.0.0.1:8080")
    wsFactory.protocol = ChatWSServerProtocol
    wsResource = WebSocketResource(wsFactory)
    return wsResource
