import telebot
import os
import time

# Render'dan gelen anahtarlar
TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

bot = telebot.TeleBot(TOKEN)

# Başlangıç bildirimi
try:
    bot.send_message(CHAT_ID, "🔍 Pathfinder Aktif ve Takipte.")
except Exception as e:
    print(f"Mesaj gönderilemedi: {e}")

# Basit bir döngü yerine botu çalıştır
print("Bot çalışıyor...")
bot.infinity_polling()








