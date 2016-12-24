# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from .Service import Service

service = Service()


class serviceHandle:
    def __init__(self, name):
        self.name = name

    def __call__(self, func):
        """
        """
        service.setTarget(self.name, func)
