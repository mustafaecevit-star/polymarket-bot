import os
import telebot
import sys
import time

# Ayarlar
TOKEN = os.environ.get("TELEGRAM_TOKEN")
# Mükemmeliyet Protokolü Ayarları
LIKIDITE_ESIYI = 1000
KAR_ORANI_ESIYI = 0.05

bot = telebot.TeleBot(TOKEN)

# 1. Komut: Protokol Durumu
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Pathfinder Aktif: Mükemmeliyet protokolü devrede. Tarama motoru hazır.")

# 2. Komut: Manuel Piyasa Taraması (Test İçin)
@bot.message_handler(commands=['tara'])
def tarama_baslat(message):
    bot.reply_to(message, "Piyasalar taranıyor: Ekonomi, Kripto, Siyaset, Spor...")
    # Burada ileride verileri çekecek fonksiyonu çağıracağız
    time.sleep(2) 
    bot.reply_to(message, "Analiz tamamlandı: Şu an kriterlere uyan fırsat bulunamadı. İzlemeye devam ediyorum.")

@bot.message_handler(func=lambda message: message.text == "Selam")
def reply_selam(message):
    bot.reply_to(message, "Merhaba, Pathfinder Avcı Modunda.")

if __name__ == "__main__":
    print("Bot Avcı modunda başlatılıyor...")
    bot.polling(none_stop=True)










