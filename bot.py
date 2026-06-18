import time
import os
import threading
import http.server
import socketserver

# MÜKEMMELİYET PROTOKOLÜ AYARLARI
LIKIDITE_ESIYI = 1000 
KAR_ORANI_ESIYI = 0.05 
SON_DAKIKA_SINIRI = 120 

def karar_mekanizmasi(piyasa_verisi):
    """Pathfinder'ın karar süzgeci."""
    print("Analiz yapılıyor...")
    
    # 1. Likidite Kontrolü
    if piyasa_verisi['hacim'] < LIKIDITE_ESIYI:
        return False
    
    # 2. Oran Analizi
    fark = piyasa_verisi['gercek_olasilik'] - piyasa_verisi['fiyat']
    if fark >= KAR_ORANI_ESIYI:
        return True
    
    return False

def market_stratejisi():
    print("Mükemmeliyet Protokolü devrede: Altın Fırsatlar bekleniyor...")
    while True:
        try:
            # Burası API'den veri aldığımız simülasyon kısmı
            piyasa_durumu = {"hacim": 1500, "fiyat": 0.40, "gercek_olasilik": 0.55, "kalan_sure": 100}
            
            # Zamanlama Kontrolü
            if piyasa_durumu['kalan_sure'] <= SON_DAKIKA_SINIRI:
                if karar_mekanizmasi(piyasa_durumu):
                    print(">>> ALTIN FIRSAT TESPİT EDİLDİ! İŞLEM BAŞARILI.")
                else:
                    print("Fırsat uygun değil, bekleniyor.")
            else:
                print(f"Piyasa olgunlaşıyor... Kalan süre: {piyasa_durumu['kalan_sure']}s")
            
            time.sleep(30)
        except Exception as e:
            print(f"Sistem hatası: {e}")
            time.sleep(10)

def start_web_server():
    class Handler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Pathfinder Bot Aktif")
    
    PORT = int(os.environ.get("PORT", 10000))
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

if __name__ == "__main__":
    threading.Thread(target=start_web_server, daemon=True).start()
    market_stratejisi()






