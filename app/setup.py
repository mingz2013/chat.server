#!/usr/bin/env python

import os
import sys

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath('.'))
from app import create_app, create_socketio

print "************* CURRENT CONFIG MODE: ", os.getenv('mingz.server.config.mode')
mode = os.getenv('mingz.server.config.mode') or 'default'
if mode:
    mode = mode.lower()
    print 'current config mode: %s' % mode

app = create_app(mode)
socketio = create_socketio(app)

if __name__ == '__main__':
    from helpers.default_encoding import init_encoding

    init_encoding()

    # app.debug = True
    # app.run(host='0.0.0.0', port=5000)
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
