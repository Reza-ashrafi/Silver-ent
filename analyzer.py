import requests
import statistics
from datetime import datetime, timedelta


# =========================
# 🧠 حافظه بازار (برای جلوگیری از نویز)
# =========================
price_history = []
last_signal_time = None
last_signal = None


# =========================
# 🥇 طلا جهانی
# =========================
def get_gold():
    try:
        r = requests.get("https://api.metals.live/v1/spot", timeout=5)
        data = r.json()
        for i in data:
            if i.get("metal") == "gold":
                return float(i.get("price"))
    except:
        pass
    return 2300


# =========================
# 🥈 نقره (مدل واقعی از طلا)
# =========================
def silver_from_gold(gold):
    gsr = statistics.mean([72, 75, 78, 82, 85])
    return gold / gsr


# =========================
# 💵 دلار
# =========================
def get_usd():
    try:
        r = requests.get(
            "https://api.exchangerate.host/latest?base=USD&symbols=IRR",
            timeout=5
        )
        return float(r.json()["rates"]["IRR"])
