# # -*- coding:utf-8 -*-
# __author__ = 'zhaojm'
#
# from flask import current_app
#
# def on_signin(self, message):
#     current_app.logger.info(message)
#     auth = message.get('auth')
#     if auth.get('token'):
#         emit(message.get('cmd'), {"retcode": 0, "result": ""})
#     else:
#         emit(message.get('cmd'), {"retcode": -1, "result": "", "errmsg": "not found token"})
#
# def on_register(self, message):
#     current_app.logger.info(message)
#     auth = message.get('auth')
#     data = message.get('data')
#     if not data:
#         emit(message.get('cmd'), {"retcode": -1, "result": "", "errmsg": "not found data"})
#         return
#     username = data.get("username")
#     password = data.get("password")
#     if not username or not password:
#         emit(message.get('cmd'), {"retcode": -1, "result": "", "errmsg": "not found username or password"})
#         return
#     token = username + password
#     auth = {"token": token}
#     emit(message.get('cmd'), {"retcode": 0, "result": auth, "errmsg": ""})
#
# def on_login(self, message):
#     current_app.logger.info(message)
#     auth = message.get('auth')
#     data = message.get('data')
#     if not data:
#         emit(message.get('cmd'), {"retcode": -1, "result": "", "errmsg": "not found data"})
#         return
#     username = data.get("username")
#     password = data.get("password")
#     if not username or not password:
#         emit(message.get('cmd'), {"retcode": -1, "result": "", "errmsg": "not found username or password"})
#         return
#     token = username + password
#     auth = {"token": token}
#     emit(message.get('cmd'), {"retcode": 0, "result": auth, "errmsg": ""})
