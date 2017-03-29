# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from ..models.message import Message
import time
from datetime import datetime


class MessageDao(object):
    def __init__(self):
        pass

    @staticmethod
    def message_add(type, send_from, send_to, content):
        ret = Message(type=type, send_from=send_from, send_to=send_to, send_time=datetime.now(), content=content).save()
        return ret

    @staticmethod
    def get_messages_for_user(user):
        return []
