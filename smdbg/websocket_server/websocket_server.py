# Author  : Matan M. Mates
# File    : websocket_server.py
# Purpose : Websocket Server for communication with the web application

from tornado import websocket

class WebSocketServer(websocket.WebSocketHandler):
    def open(self):
        print 'Websocket opened'

    def on_message(self, message):
        self.write_message(u'Recieved:' + message)
        
    def on_close(self):
        print "Websocket closed"
         
