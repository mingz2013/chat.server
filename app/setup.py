#!/usr/bin/env python

import os
import sys

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath('.'))


if __name__ == '__main__':
    from app.core.default_encoding import init_encoding

    init_encoding()

    from app import Server
    from app.webapp import webapp

    print "run on 0.0.0.0:5000"
    Server().run(webapp, host="0.0.0.0", port=5000, reload=True)
