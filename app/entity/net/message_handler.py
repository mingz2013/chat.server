# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from conn_manager import ConnectionManager


class MessageHandler(object):
    def __init__(self):
        self._handlers = {}

        self.connManager = ConnectionManager()

    def on(self, event, handler=None):
        print "on.."

        def set_handler(handler):
            self._handlers[event] = handler
            return handler

        if handler is None:
            return set_handler
        set_handler(handler)

    def handle_message(self, sid, message):
        print "handle_message"
        cmd = message.get('cmd')
        data = message.get('data')
        conn = self.connManager.getConnection(sid)
        return self._trigger_event(cmd, conn, data)

    def _trigger_event(self, event, conn, data):
        """Invoke an event handler."""
        if event in self._handlers:
            # if async:
            #     return self.start_background_task(self.handlers[event], *args)
            # else:
            #     return self.handlers[event](*args)
            return self._handlers[event](conn, data)


msgHandler = MessageHandler()
from ..handlers import *

__all__ = [msgHandler]
