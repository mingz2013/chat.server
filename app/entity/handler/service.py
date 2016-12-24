# -*- coding:utf-8 -*-
__author__ = 'zhaojm'


class Service(object):
    def __init__(self):
        """
        """
        self.targets = {}

    def setTarget(self, name, func):
        """
        """
        assert not self.targets.has_key(name)
        self.targets[name] = func

    def unSetTarget(self, name):
        """
        """
        assert self.targets.has_key(name)
        del self.targets[name]

    def call(self, name, *args, **kw):
        """
        """
        assert self.targets.has_key(name)
        response = self.targets[name](*args, **kw)
        # response["data"] = response.get("data", "")
        return response



