# analyzer.py

from indicators import ema, rsi, macd, momentum, atr, bollinger_width
from score_engine import final_score
from signal_engine import generate_signal


# =========================
# MAIN ANALYZE FUNCTION
# =========================
def analyze(market_data):
    """
    market_data باید اینا رو داشته باشه:

    {
        prices: [],
        highs: [],
        lows: [],
        closes: [],
        bubble: float
    }
    """

    prices = market_data["prices"]
    highs = market_data["highs"]
    lows = market_data["lows"]
    closes = market_data["closes"]
    bubble = market_data["bubble"]

    # =========================
    # INDICATORS
    # =========================
    ema20 = ema(prices, 20)
    ema50 = ema(prices, 50)

    rsi_val = rsi(prices)
    macd_val = macd(prices)

    momentum_val = momentum(prices)
    atr_val = atr(highs, lows, closes)
    boll_val = bollinger_width(prices)

    # =========================
    # SCORE ENGINE
    # =========================
    scores = final_score({
        "ema20": ema20,
        "ema50": ema50,
        "bubble": bubble,
        "rsi": rsi_val,
        "macd": macd_val,
        "atr": atr_val,
        "bollinger_width": boll_val
    })

    # =========================
    # SIGNAL ENGINE
    # =========================
    signal_data = generate_signal(scores)

    # =========================
    # ENTRY METER (ساده ولی مهم)
    # =========================
    entry_meter = scores["total_score"]

    if entry_meter > 85:
        entry_text = "🟢 نقطه ورود عالی"
    elif entry_meter > 70:
        entry_text = "🟡 ورود پله‌ای"
    elif entry_meter > 55:
        entry_text = "⚠️ صبر کن"
    else:
        entry_text = "🔴 ورود ممنوع"

    # =========================
    # REPORT
    # =========================
    return {
        "scores": scores,
        "signal": signal_data["signal"],
        "capital": signal_data["capital"],
        "confidence": signal_data["confidence"],
        "entry_meter": entry_meter,
        "entry_text": entry_text,
        "indicators": {
            "ema20": ema20,
            "ema50": ema50,
            "rsi": rsi_val,
            "macd": macd_val,
            "momentum": momentum_val,
            "atr": atr_val,
            "bollinger": boll_val
        }
    }
