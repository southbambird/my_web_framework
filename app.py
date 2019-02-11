import re

def http404(env, start_response):
    start_response('404 Not Found', [('Content-type', 'text/plain; charset=utf08')])
    return [b'404 Not Found']

class Router:
    def __init__(self):
        self.routes = []

    def add(self, method, path, callback):
        self.routes.append({
            'method': method,
            'path': path,
            'callback': callback,
        })

    def match(self, method, path):
        for r in self.routes:
            matched = re.compile(r['path']).match(path)
            if matched and r['method'] == method:
                url_vars = matched.groupdict()
                return r['callback'], url_vars
        return http404, {}
