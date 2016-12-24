# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from flask import request
from flask_socketio import Namespace
from .ConnectionManager import ConnectionManager
from ..handler.serviceHandle import service


class ChatNamespace(Namespace):
    def __init__(self, namespace=None):
        super(Namespace, self).__init__(namespace)
        self.connectionManager = ConnectionManager()
        pass

    def on_connect(self):
        print "on connect id", request.sid
        self.connectionManager.addConnection(request.sid)

    def on_disconnect(self):
        print 'on disconnect', request.sid
        self.connectionManager.dropConnectionByID(request.sid)

    def on_error(self, e):
        print "on error"
        print e

    def on_message(self, message):  # send
        print "on message...", request.sid
        print message
        # cmd = message.get("cmd")
        # data = message.get("data")
        # print cmd
        # print data
        # conn = self.connectionManager.getConnectionByID(request.sid)
        # response = service.call(conn, message)
        # self.send(response)
        self.send(message)


        # def on_anything(self, message):
        #     print "on anything..."
        #     print message
        #
        # def on_json(self, json):
        #     print "on json..."
        #     print json
        #
        # def on_my_event(self, message):
        #     print "on my event"
        #     print message
