# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from ..models.user import User


class UserDao(object):
    def __init__(self):
        pass

    @staticmethod
    def add_user(username, password):
        ret = User(username, password).save()
        print ret

    @staticmethod
    def check_login(username, password):
        return True
