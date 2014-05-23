import unittest
from smdbg.http_server import HTTPServer
import tornado.ioloop
import os
from threading import Thread
from time import sleep
import urllib2
    
PORT = 8383
 
class TestWebServer(unittest.TestCase):
    def setUp(self):
        server = HTTPServer(PORT, "web" + os.sep) 
        server.start()
        self._server_thread = \
        Thread(target=tornado.ioloop.IOLoop.instance().start)
        self._server_thread.daemon = True
        self._server_thread.start()
                
    def test_page(self):
        req = urllib2.urlopen('http://127.0.0.1:' + str(PORT) + '/test.html')
        self.assertTrue('#mark#' in req.read())
        self.assertEquals(req.code, 200)
    
    def tearDown(self):
        tornado.ioloop.IOLoop.instance().stop()
        self._server_thread.join()

