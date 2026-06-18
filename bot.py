
import os
import time
import threading
import http.server
import socketserver

PORT = int(os.environ.get("PORT", 10000))

def market_stratejisi():
    print("Mukemmeliyet Protokolu baslatildi: Piyasa izleniyor...")
    while True:
        try:
            print("Piyasa verileri taraniyor, golden opportunity araniyor...")
            time.sleep(60)
        except Exception as e:
            print(f"Hata olustu: {e}")
            time.sleep(10)

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot Aktif - Mukemmeliyet Protokolu Devrede")

def start_web_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Web kapisi {PORT} portunda acik.")
        httpd.serve_forever()

if __name__ == "__main__":
    threading.Thread(target=start_web_server, daemon=True).start()
    market_stratejisi()


