#!/usr/bin/python3

"""Using http.server to create a simple HTTP server."""

import http.server
import socketserver

def main():
    """run-time code"""

    port = 9021

    handler = http.server.SimpleHTTPRequestHandler

    httpd = socketserver.TCPServer(("", port), handler)

    print(("serving at port", port))

    httpd.serve_forever()

if __name__ == "__main__":
    main()
