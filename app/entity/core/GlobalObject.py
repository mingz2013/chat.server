# -*- coding:utf-8 -*-
__author__ = 'zhaojm'


class GlobalObject(object):
    def __init__(self):
        self.configInstance = None
        self.connectionManagerInstance = None
        pass

    def setConfig(self, config):
        self.configInstance = config

    def setConnectionManager(self, connectionManager):
        self.connectionManagerInstance = connectionManager
