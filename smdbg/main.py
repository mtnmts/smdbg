# Author   : Matan M. Mates
# File     : main.py
# Purpose  : Run the SMDBG Server

import config
import handlers
import tornado.ioloop
import tornado.web
import tornado.httpserver
import os

def build_application():
    application = tornado.web.Application([
    (r'/smdbg/(.*)', handlers.WebStaticHandler, {'path' : config.SERVE_PATH}),
    (r'/ws', handlers.WebSocketHandler)])
    return application

def main():
    app = build_application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
    
     
if __name__ == '__main__':
    main()
