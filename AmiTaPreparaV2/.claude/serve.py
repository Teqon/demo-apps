import functools
import http.server
import socketserver

DIR = "/Users/rich/Documents/GitHub/demo-apps/AmiTaPreparaClaude"
Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=DIR)
with socketserver.TCPServer(("127.0.0.1", 4173), Handler) as httpd:
    httpd.serve_forever()
