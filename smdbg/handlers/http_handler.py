# Author  : Matan M. Mates
# File    : http_handler.py
# Purpose : HTTP handler serving the web application

import subprocess
import tornado.web
import tornado.httpserver
import os


class WebStaticHandler(tornado.web.StaticFileHandler):
    pass
