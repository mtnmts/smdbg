# Author  : Matan M. Mates
# File    : websocket_handler.py
# Purpose : Websocket handler for communication with the web application

from tornado import websocket

class WebSocketHandler(websocket.WebSocketHandler):
    def open(self):
        print 'Websocket opened'

    def on_message(self, message):
        print "Message recieved of length: {}".format(str(len(message)))
        self.write_message(u'Recieved:' + message)
        
    def on_close(self):
        print "Websocket closed"
         
