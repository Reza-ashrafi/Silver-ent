# main.py

import time
from datetime import datetime

from analyzer import analyze
from telegram_sender import send_report


# =========================
# MOCK DATA (فعلاً دیتای واقعی بازار)
# بعداً اینو به API وصل می‌کنیم
# =========================
def get_market_data():

    # اینجا فعلاً دیتا نمونه است
    # بعداً از API واقعی یا بورس جایگزین میشه

    prices = [100, 101, 102, 101, 103, 104, 105, 106, 107, 108,
              109, 110, 111, 112, 113, 114, 115]

    highs = [p + 1 for p in prices]
    lows = [p - 1 for p in prices]
    closes = prices

    bubble = 3.5  # فعلاً فرضی (بعداً واقعی میشه)

    return {
        "prices": prices,
        "highs": highs,
        "lows": lows,
        "closes": closes,
        "bubble": bubble
    }


# =========================
# CHECK MARKET HOURS
# =========================
def is_market_open():
    hour = datetime.now().hour
    return 12 <= hour <= 17


# =========================
# RUN ENGINE
# =========================
def run_bot():

    print("SilverMind Pro Started...")

    last_signal = None

    while True:

        try:
            if not is_market_open():
                print("Market Closed - Waiting...")
                time.sleep(300)
                continue

            market_data = get_market_data()

            result = analyze(market_data)

            if not result:
                print("No signal generated")
                time.sleep(300)
                continue

            signal = result["signal"]

            # =========================
            # FILTER: فقط تغییر سیگنال ارسال شود
            # =========================
            if signal != last_signal:
                send_report(result)
                last_signal = signal
                print("Signal Sent:", signal)
            else:
                print("No change:", signal)

            time.sleep(300)  # هر 5 دقیقه بررسی

        except Exception as e:
            print("Error:", e)
            time.sleep(60)


# =========================
# START
# =========================
if __name__ == "__main__":
    run_bot()
