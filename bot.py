import os
import telebot
import sys

# 1. Ortam Değişkenlerini Tanımla
TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

# 2. Güvenlik Kontrolü
if not TOKEN:
    print("KRİTİK HATA: TELEGRAM_TOKEN bulunamadı!")
    sys.exit(1)

# 3. Botu Başlat
bot = telebot.TeleBot(TOKEN)

# 4. Mükemmeliyet Protokolü ve Komutlar
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Pathfinder Aktif: Mükemmeliyet protokolü devrede.")

@bot.message_handler(func=lambda message: message.text == "Selam")
def reply_selam(message):
    bot.reply_to(message, "Merhaba, Pathfinder Aktif ve Takipte.")

# 5. Botun Sürekli Çalışmasını Sağlayan Döngü
if __name__ == "__main__":
    print("Bot başlatılıyor ve bağlantı kuruluyor...")
    # none_stop=True, botun hatalarda durmamasını sağlar
    bot.polling(none_stop=True)









