print("🔥 BOT IS STARTING")

from telegram_sender import send_report

print("📦 IMPORT OK")

try:
    send_report()
    print("📲 MESSAGE SENT OK")
except Exception as e:
    print("❌ ERROR:", e)

print("🏁 BOT FINISHED")
