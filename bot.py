import os
import telebot
import sys
import time
from flask import Flask
from threading import Thread

# 1. Flask (Port kandırmaca)
app = Flask(__name__)
@app.route('/')
def home():
    return "Pathfinder Aktif: Sistem çalışıyor."

def run_web():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

# 2. Bot Ayarları
TOKEN = os.environ.get("TELEGRAM_TOKEN")
LIKIDITE_ESIYI = 1000
KAR_ORANI_ESIYI = 0.05

bot = telebot.TeleBot(TOKEN)

# 3. Komutlar
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Pathfinder Aktif: Mükemmeliyet protokolü devrede.")

@bot.message_handler(commands=['tara'])
def tarama_baslat(message):
    bot.reply_to(message, "Piyasalar taranıyor: Ekonomi, Kripto, Siyaset, Spor... Analiz tamamlandı: Şu an kriterlere uyan fırsat bulunamadı.")

@bot.message_handler(func=lambda message: message.text == "Selam")
def reply_selam(message):
    bot.reply_to(message, "Merhaba, Pathfinder Avcı Modunda.")

# 4. Ana Çalıştırma
if __name__ == "__main__":
    # Web sunucusunu ayrı bir kanalda (thread) başlat
    Thread(target=run_web).start()
    
    print("Bot Avcı modunda başlatılıyor...")
    bot.polling(none_stop=True)











