import asyncio
from telegram import Bot
from config import BOT_TOKEN, CHAT_ID
from analyzer import analyze

bot = Bot(token=BOT_TOKEN)


def build_message(data):
    return f"""
📊 گزارش نقره
🌍 قیمت: {data.get('silver', 0)}
"""


async def send_async():
    data = analyze()
    msg = build_message(data)
    await bot.send_message(chat_id=CHAT_ID, text=msg)


def send_report():
    asyncio.run(send_async())
