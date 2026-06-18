import http.server
import socketserver
import os

print("Polymarket Botu Basariyla Calisti!")

# Render'in istedigi sahte web kapisi (port) ayari
PORT = int(os.environ.get("PORT", 10000))
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Sahte sunucu {PORT} portunda aktif.")
    httpd.serve_forever()

