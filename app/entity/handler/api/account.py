# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from .. import ServiceHandle


@ServiceHandle("login")
def login(conn, data):
    print data
    pass
