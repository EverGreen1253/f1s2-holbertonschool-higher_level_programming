#!/usr/bin/python3
""" Nameless module for Task 3 """


import json
from functools import cached_property
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qsl, urlparse
from http.server import HTTPServer, SimpleHTTPRequestHandler

class WebRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # self.wfile.write(self.get_response().encode("utf-8"))
        if self.path == '/':
            # Step 1
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()

            self.wfile.write(bytes("Hello, this is a simple API!\n", 'UTF-8'))
        elif self.path == '/data':
            # Step 2
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(bytes('{"name": "John", "age": 30, "city": "New York"}', 'UTF-8'))
        elif self.path == '/info':
            # Step 3
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            d = json.dumps({"version": "1.0", "description": "A simple API built with http.server"})
            self.wfile.write(bytes(d, 'UTF-8'))
        else:
            # Step 4
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()

            self.wfile.write(bytes("<html><head><title> 404 - Page Not Found </title></head><body><h1>Endpoint not found</h1></body></html>", 'UTF-8'))

    # def do_POST(self):
    #     self.do_GET()


if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), WebRequestHandler)
    print("Web server started at localhost:8000")
    server.serve_forever()
