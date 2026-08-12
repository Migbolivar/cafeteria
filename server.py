#!/usr/bin/env python3
"""Cafetería demo — servidor multi-hilo (patrón ganador: ThreadingTCPServer)."""
import http.server, socketserver, os

PORT = 8905
DIR = '/root/web-animadas/cafeteria'

class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=DIR, **kw)
    def log_message(self, *a):
        pass

if __name__ == '__main__':
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(('0.0.0.0', PORT), H) as s:
        print(f'cafeteria en :{PORT}')
        s.serve_forever()
