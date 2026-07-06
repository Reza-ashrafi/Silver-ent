import requests


# =========================
# 🥈 قیمت نقره جهانی
# =========================
def get_silver_price():
    try:
        url = "https://api.metals.live/v1/spot"
        r = requests.get(url, timeout=5)
        data = r.json()

        for item in data:
            if item.get("metal") == "silver":
                return float(item.get("price"))
    except:
        pass

    return 28.5  # fallback امن


# =========================
# 💵 دلار واقعی (IRR → Toman)
# =========================
def get_usd_price():
    try:
        url = "https://api.exchangerate.host/latest?base=USD&symbols=IRR"
        r = requests.get(url, timeout=5)
        data = r.json()

        irr = data["rates"]["IRR"]
        return float(irr) / 10  # تبدیل ریال به تومان
    except:
        return 600000  # fallback امن


# =========================
# 📊 محاسبه قیمت ذاتی
# =========================
def intrinsic_value(silver, usd):
    return (silver * usd * 31.1) / 1000


# =========================
# 💣 محاسبه حباب ایران
# =========================
def calculate_bubble(intrinsic, market):
    return ((market - intrinsic) / intrinsic) * 100


# =========================
# 🧠 تحلیل اصلی و سیگنال
# =========================
def analyze():

    silver = get_silver_price()
    usd = get_usd_price()

    intrinsic = intrinsic_value(silver, usd)

    # مدل بازار ایران (اگر قیمت واقعی نداری)
    market = intrinsic * 1.08

    bubble = calculate_bubble(intrinsic, market)

    # امتیاز خرید
    score = 100 - abs(bubble) * 2
    score = max(0, min(100, score))

    # =========================
    # 🚦 سیگنال حرفه‌ای
    # =========================
    if bubble < 3:
        signal = "🟢 خرید قوی (ارزشمند)"
    elif bubble < 8:
        signal = "🟢 ورود پله‌ای مناسب"
    elif bubble < 15:
        signal = "🟡 صبر یا خرید سبک"
    elif bubble < 25:
        signal = "🔴 پرریسک - اصلاح محتمل"
    else:
        signal = "🔴 حباب بالا - ورود ممنوع"

    return {
        "silver": silver,
        "usd": usd,
        "intrinsic": intrinsic,
        "market": market,
        "bubble": bubble,
        "score": score,
        "signal": signal
    }
