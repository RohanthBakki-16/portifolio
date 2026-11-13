#!/usr/bin/env python3
"""
Rohanth Bakki Portfolio — Local Development Server
Lightweight, zero-dependency HTTP server with correct MIME types and auto-reload support.
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class PortfolioHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Enable CORS and caching headers for dev
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def guess_type(self, path):
        # Explicit MIME types for modern web assets
        if path.endswith('.js'):
            return 'application/javascript'
        if path.endswith('.css'):
            return 'text/css'
        if path.endswith('.svg'):
            return 'image/svg+xml'
        if path.endswith('.json'):
            return 'application/json'
        if path.endswith('.jpg') or path.endswith('.jpeg'):
            return 'image/jpeg'
        if path.endswith('.png'):
            return 'image/png'
        return super().guess_type(path)

def run_server():
    port = PORT
    for _ in range(10):
        try:
            with socketserver.TCPServer(("", port), PortfolioHTTPRequestHandler) as httpd:
                url = f"http://localhost:{port}"
                print("=" * 65)
                print(f"✨ ROHANTH BAKKI — 3D PORTFOLIO SERVER RUNNING")
                print(f"🌐 Local URL:  {url}")
                print(f"📁 Root:       {DIRECTORY}")
                print("=" * 65)
                print("Press Ctrl+C to stop the server.\n")

                if "--open" in sys.argv:
                    webbrowser.open(url)

                httpd.serve_forever()
                break
        except OSError:
            print(f"Port {port} in use, trying {port + 1}...")
            port += 1

if __name__ == '__main__':
    run_server()
