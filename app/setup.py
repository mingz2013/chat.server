#!/usr/bin/env python

import os
import sys
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath('.'))

print "************* CURRENT CONFIG MODE: ", os.getenv('mingz.server.config.mode')
mode = os.getenv('mingz.server.config.mode') or 'default'
if mode:
    mode = mode.lower()
    print 'current config mode: %s' % mode

from app import create_app, eio
app = create_app(mode)


def run_server():
    if eio.async_mode == 'threading':
        # deploy with Werkzeug
        app.run(threaded=True)
    elif eio.async_mode == 'eventlet':
        # deploy with eventlet
        import eventlet
        from eventlet import wsgi
        wsgi.server(eventlet.listen(('', 5000)), app)
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
            pywsgi.WSGIServer(('', 5000), app,
                              handler_class=WebSocketHandler).serve_forever()
        else:
            pywsgi.WSGIServer(('', 5000), app).serve_forever()
    else:
        print('Unknown async_mode: ' + eio.async_mode)


if __name__ == '__main__':
    from helpers.default_encoding import init_encoding
    init_encoding()

    # app.debug = True
    # app.run(host='0.0.0.0', port=5000)
    # socketio.run(app, host='0.0.0.0', port=5000, debug=True)
    # from gevent import pywsgi
    # from geventwebsocket.handler import WebSocketHandler
    # server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    # server.serve_forever()
    if reload:
        from werkzeug.serving import run_with_reloader

        run_with_reloader(run_server)
    else:
        run_server()
