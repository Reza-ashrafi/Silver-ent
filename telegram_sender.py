import asyncio
from telegram import Bot
from config import BOT_TOKEN, CHAT_ID
from analyzer import analyze

bot = Bot(token=BOT_TOKEN)


def build_message(data):
    if "error" in data:
        return "❌ داده‌ها در دسترس نیستند"

    return f"""
📊 گزارش روزانه نقره

🌍 قیمت جهانی: {data['silver']:.2f} $
💵 دلار: {int(data['usd']):,} تومان

📦 ارزش ذاتی: {int(data['intrinsic']):,}
⚖️ ارزش منصفانه: {int(data['fair_value']):,}

🏪 قیمت بازار: {int(data['market']):,}

📈 حباب: {data['bubble']:.2f}%
⭐ امتیاز: {data['score']:.0f}/100

{data['decision']}
"""


async def send_async():
    data = analyze()
    msg = build_message(data)
    await bot.send_message(chat_id=CHAT_ID, text=msg)


def send_report():
    asyncio.run(send_async())
    
