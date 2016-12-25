# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from ..models.message import Message


class MessageDao(object):
    def __init__(self):
        pass

    @staticmethod
    def message_add(type, send_from, send_to):
        # Message(type=type, send_from=send_from, send_to=send_to, send_time=)
        return True

    @staticmethod
    def get_messages_for_user(user):
        return []
