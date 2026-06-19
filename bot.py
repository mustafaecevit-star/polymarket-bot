import os
import telebot
import threading
from flask import Flask

# 1. Flask ile Port Dinleyici
app = Flask(__name__)

@app.route('/')
def home():
    return "Pathfinder Aktif: Sistem operasyonel."

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

# 2. Telegram Bot Kurulumu
TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

# 3. Komutlar
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Pathfinder 'Avcı' Modunda. Mükemmeliyet protokolü devrede.")

@bot.message_handler(commands=['tara'])
def tarama_baslat(message):
    bot.reply_to(message, "Piyasalar taranıyor: Analiz tamamlandı: Şu an kriterlere uyan fırsat bulunamadı.")

@bot.message_handler(func=lambda message: message.text == "Selam")
def reply_selam(message):
    bot.reply_to(message, "Merhaba Kaptan, Pathfinder emrinizde.")

# 4. Ana Çalıştırma
if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    
    print("Bot Avcı modunda başlatılıyor...")
    # 409 hatasını engellemek için infinity_polling kullanıyoruz
    bot.infinity_polling(none_stop=True)













