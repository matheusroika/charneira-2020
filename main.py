import os
from charneira.app import app as charneira_app
from config import BaseConfig
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from threading import Lock
from werkzeug.exceptions import NotFound

class MySubdomainDispatcher(object):

    def __init__(self, domain):
        self.domain = domain
        self.lock = Lock()
        self.instances = {
            '': charneira_app,
            'www': charneira_app,
            }

    def get_application(self, host):
        host = host.split(':')[0]
        assert host.endswith(self.domain), 'Configuration error'
        subdomain = host[:-len(self.domain)].rstrip('.')
        with self.lock:
            app = self.instances.get(subdomain)
            if app is None:
                return NotFound()
            return app

    def __call__(self, environ, start_response):
        app = self.get_application(environ['HTTP_HOST'])
        return app(environ, start_response)

app = MySubdomainDispatcher(BaseConfig.uri)

if __name__ == '__main__':
    if BaseConfig.ENV == 'development':
        run_simple('0.0.0.0', 5000, app, use_debugger=True, use_reloader=True, use_evalex=True, ssl_context=('./cert.pem', './key.pem'))
    else:
        port = int(os.environ.get("PORT", 5000))
        run_simple('0.0.0.0', port, app, use_debugger=True, use_reloader=True, use_evalex=True)