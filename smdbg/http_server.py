# Author  : Matan M. Mates
# File    : http_server.py
# Purpose : HTTP Server serving the web application

import subprocess
import tornado.web
import tornado.httpserver
import os


class HTTPServer(object):

    def __init__(self, port, serve_path):
        self._port = port
        self._running = False
        self._serve_path = serve_path

        @property
        def port(self):
            return self._port


        def start(self):
            """ Starts the HTTP Server if it wasn't running,
            calling this function if the server is already
            running will do nothing """
            settings = {'static_path' : self._serve_path}
            handlers = [(r'/(.*)', tornado.web.StaticFileHandler, {'path' : self._serve_path})]      
            app = tornado.web.Application(handlers, **settings)
            server = tornado.httpserver.HTTPServer(app) 
            server.listen(self._port)

            @property
            def running():
                return self._running
