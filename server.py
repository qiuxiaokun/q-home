#encode:utf8
from app import app
from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
import sys

_app = DispatcherMiddleware(
        app, {
        }
    )

if __name__=='__main__':
    port = 8888
    if 'debug' in sys.argv:
        port = 7777
    run_simple('0.0.0.0', port, _app, use_reloader=False,  use_debugger=True, threaded=True)
