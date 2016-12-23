from flask import request
from flask_socketio import Namespace


class ChatNamespace(Namespace):
    def on_connect(self):
        print "on connect id", request.sid

    def on_disconnect(self):
        print 'on disconnect', request.sid

    def on_message(self, message):
        print "on message..."
        print message

    def on_anything(self, message):
        print "on anything..."
        print message

    def on_json(self, json):
        print "on json..."
        print json

    def on_error(self, e):
        print "on error"
        print e

    def on_my_event(self, message):
        print "on my event"
        print message
