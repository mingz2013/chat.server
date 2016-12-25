# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import engineio

async_mode = 'gevent'
eio = engineio.Server(async_mode=async_mode)
from app.entity.net import eio_controller

from mongoengine import connect

connect('chat')


class Server(object):
    def __init__(self):
        pass

    def run(self,
            app,
            port=5000,
            reload=True
            ):
        def _run_server():
            if eio.async_mode == 'threading':
                # deploy with Werkzeug
                app.run(threaded=True)
            elif eio.async_mode == 'eventlet':
                # deploy with eventlet
                import eventlet
                from eventlet import wsgi
                wsgi.server(eventlet.listen(('', port)), app)
            elif eio.async_mode == 'gevent':
                # deploy with gevent
                from gevent import monkey
                monkey.patch_all()
                from gevent import pywsgi
                try:
                    from geventwebsocket.handler import WebSocketHandler
                    websocket = True
                except ImportError:
                    websocket = False
                if websocket:
                    pywsgi.WSGIServer(('', port), app, handler_class=WebSocketHandler).serve_forever()
                else:
                    pywsgi.WSGIServer(('', port), app).serve_forever()
            elif eio.async_mode == 'gevent_uwsgi':
                print('Start the application through the uwsgi server. Example:')
                print('uwsgi --http :5000 --gevent 1000 --http-websockets --master --wsgi-file app.py --callable app')
            else:
                print('Unknown async_mode: ' + eio.async_mode)

        app.wsgi_app = engineio.Middleware(eio, app.wsgi_app)

        if reload:
            from werkzeug.serving import run_with_reloader
            run_with_reloader(_run_server)
        else:
            _run_server()
