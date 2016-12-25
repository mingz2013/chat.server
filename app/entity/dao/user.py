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
        user = User.objects(username=username, password=password).first()
        return user

    @staticmethod
    def get_user_list():
        user_list = User.objects
        return user_list

    @staticmethod
    def find_user_by_username(username):
        user = User.objects(username=username).first()
        return user
