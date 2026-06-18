import os
import time
import threading
import http.server
import socketserver

PORT = int(os.environ.get("PORT", 10000))

def market_stratejisi():
    print("Mukemmeliyet Protokolu baslatildi")
    while True:
        try:
            print("Piyasa izleniyor")
            time.sleep(60)
        except Exception:
            time.sleep(10)

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot Aktif")

def start_web_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

if __name__ == "__main__":
    threading.Thread(target=start_web_server, daemon=True).start()
    market_stratejisi()




