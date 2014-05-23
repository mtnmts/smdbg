# Author  : Matan M. Mates
# File    : http_server.py
# Purpose : HTTP Server serving the web application

class HTTPServer(object):
    import subprocess
    from tornado.web import StaticFileHandler
    
    SERVE_PATH = "web" + os.sep

    def __init__(self, port, serve_path):
        self._port = port
        self._running = False

    @property
    def port(self):
        return self._port
         

    def start(self):
        """ Starts the HTTP Server if it wasn't running,
            calling this function if the server is already
            running will do nothing """
        settings = {'static_path' : SERVE_PATH}
        handlers = [(r'/(.*)', StaticFileHandler, {'path' : SERVE_PATH})]      
    @property
    def running():
        return self._running
