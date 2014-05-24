# Author   : Matan M. Mates
# File     : main.py
# Purpose  : Run the SMDBG Server

from http_server import HTTPServer
import tornado.ioloop
import os

def startHTTPServer():
   serv = HTTPServer('web' + os.sep) 
   serv.start()

def main():
    startHTTPServer()
    tornado.ioloop.IOLoop.instance().start()
   
if __name__ == '__main__':
    main()
