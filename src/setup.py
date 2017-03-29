#!/usr/bin/env python

import os
import sys

# current_path = os.path.dirname(os.path.abspath(__file__))
# source_path = os.path.join(current_path, "../../")
# sys.path.append(os.path.join(source_path, "difang/src/"))
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath('.'))


if __name__ == '__main__':
    from app.core.default_encoding import init_encoding

    init_encoding()

    from app import Server
    from webapp import webapp

    print "run on 0.0.0.0:5000"
    Server().run(webapp, host="0.0.0.0", port=5000, reload=True)
