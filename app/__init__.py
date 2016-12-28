# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

async_mode = 'gevent'
# 控制用engineio 还是socketio
# import engineio as _io
import socketio as _io

io = _io.Server(logger=True, async_mode=async_mode)
from .net import io_controller

from mongoengine import connect

connect('chat')


class Server(object):
    def __init__(self):
        pass

    def run(self,
            app,
            host='localhost',
            port=5000,
            reload=True
            ):
        def _run_server():
            if io.async_mode == 'threading':
                # deploy with Werkzeug
                app.run(threaded=True)
            elif io.async_mode == 'eventlet':
                # deploy with eventlet
                import eventlet
                import eventlet.wsgi
                eventlet.wsgi.server(eventlet.listen((host, port)), app)
            elif io.async_mode == 'gevent':
                # deploy with gevent
                from gevent import pywsgi
                try:
                    from geventwebsocket.handler import WebSocketHandler
                    websocket = True
                except ImportError:
                    websocket = False
                if websocket:
                    pywsgi.WSGIServer((host, port), app, handler_class=WebSocketHandler).serve_forever()
                else:
                    pywsgi.WSGIServer((host, port), app).serve_forever()
            elif io.async_mode == 'gevent_uwsgi':
                print('Start the application through the uwsgi server. Example:')
                print('uwsgi --http :5000 --gevent 1000 --http-websockets --master --wsgi-file app.py --callable app')
            else:
                print('Unknown async_mode: ' + io.async_mode)

        app.wsgi_app = _io.Middleware(io, app.wsgi_app)

        if reload:
            from werkzeug.serving import run_with_reloader
            run_with_reloader(_run_server)
        else:
            _run_server()
