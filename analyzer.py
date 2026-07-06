import requests


# =========================
# 🥈 قیمت نقره (Multi-source)
# =========================
def get_silver_price():

    # 🔹 منبع 1
    try:
        url = "https://api.metals.live/v1/spot"
        r = requests.get(url, timeout=5)
        data = r.json()

        for item in data:
            if item.get("metal") == "silver":
                price = float(item.get("price"))
                if price > 0:
                    return price
    except:
        pass

    # 🔹 منبع 2
    try:
        url = "https://www.goldapi.io/api/XAG/USD"
        headers = {"x-access-token": "demo"}

        r = requests.get(url, headers=headers, timeout=5)
        data = r.json()

        if "price" in data:
            price = float(data["price"])
            if price > 0:
                return price
    except:
        pass

    # ❌ اگر هیچ منبعی جواب نداد
    return None


# =========================
# 💵 قیمت دلار
# =========================
def get_usd_price():
    try:
        url = "https://api.exchangerate.host/latest?base=USD&symbols=IRR"
        r = requests.get(url, timeout=5)
        data = r.json()

        irr = data["rates"]["IRR"]
        return float(irr) / 10  # ریال → تومان

    except:
        return 600000  # fallback


# =========================
# 📦 قیمت ذاتی
# =========================
def intrinsic_value(silver, usd):
    return (silver * usd * 31.1) / 1000


# =========================
# 💣 حباب ایران
# =========================
def calculate_bubble(intrinsic, market):
    return ((market - intrinsic) / intrinsic) * 100


# =========================
# 🧠 تحلیل نهایی + سیگنال
# =========================
def analyze():

    silver = get_silver_price()

    # اگر دیتا نبود
    if silver is None:
        return {
            "silver": "NO DATA",
            "usd": 0,
            "intrinsic": 0,
            "market": 0,
            "bubble": 0,
            "score": 0,
            "signal": "🔴 عدم دریافت دیتا از منابع"
        }

    usd = get_usd_price()

    intrinsic = intrinsic_value(silver, usd)

    # مدل بازار ایران (تخمینی)
    market = intrinsic * 1.08

    bubble = calculate_bubble(intrinsic, market)

    score = 100 - abs(bubble) * 2
    score = max(0, min(100, score))

    # =========================
    # 🚦 سیگنال حرفه‌ای
    # =========================
    if bubble < 3:
        signal = "🟢 خرید قوی"
    elif bubble < 8:
        signal = "🟢 ورود پله‌ای"
    elif bubble < 15:
        signal = "🟡 صبر / خرید سبک"
    elif bubble < 25:
        signal = "🔴 پرریسک"
    else:
        signal = "🔴 حباب بالا - عدم ورود"

    return {
        "silver": silver,
        "usd": usd,
        "intrinsic": intrinsic,
        "market": market,
        "bubble": bubble,
        "score": score,
        "signal": signal
    }
