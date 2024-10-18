#!/usr/bin/python3
import http.server
import socketserver
import json

PORT = 8000

class Holberton_API(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"name": "John", "age": 30, "city": "New York"}).encode())
        elif self.path == '/status':
            self.send_response(200)
            self.wfile.write(b"OK")
        elif self.path == '/info':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"version": "1.0", "description": "A simple API built with http.server"}).encode())
        else:
            self.send_response(404)
            self.wfile.write(b"Endpoint not found")


with socketserver.TCPServer(("", PORT), Holberton_API) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
