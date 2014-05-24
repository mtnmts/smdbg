# Author  : Matan M. Mates
# File    : http_handler.py
# Purpose : HTTP handler serving the web application

import subprocess
import tornado.web
import tornado.httpserver
import os


class WebStaticHandler(tornado.web.StaticFileHandler):
    def parse_url_path(self, url_path):
        if not url_path or url_path == '/':
            url_path += 'main.html'
