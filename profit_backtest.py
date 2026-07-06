# profit_backtest.py

import pandas as pd
from analyzer import analyze


# =========================
# LOAD REAL CSV DATA
# =========================
def load_data(path="data.csv"):
    df = pd.read_csv(path)
    return df["price"].tolist()


# =========================
# SIMPLE TRADING STRATEGY
# =========================
def run_profit_backtest():

    prices = load_data()

    if len(prices) < 50:
        print("❌ Not enough data")
        return

    position = 0
    entry_price = 0

    trades = []
    equity = 100  # فرض سرمایه اولیه

    for i in range(30, len(prices)):

        window = prices[i-30:i]

        data = {
            "prices": window,
            "highs": [p * 1.01 for p in window],
            "lows": [p * 0.99 for p in window],
            "closes": window,
            "bubble": (window[-1] - window[0]) / window[0] * 100
        }

        result = analyze(data)
        signal = result["signal"]

        price = prices[i]

        # =========================
        # ENTRY
        # =========================
        if signal in ["BUY", "STRONG_BUY"] and position == 0:
            position = 1
            entry_price = price
            print(f"BUY @ {price}")

        # =========================
        # EXIT
        # =========================
        elif signal in ["RISK", "NO_TRADE"] and position == 1:
            profit = ((price - entry_price) / entry_price) * 100
            equity += equity * (profit / 100)

            trades.append(profit)

            print(f"SELL @ {price} | Profit: {profit:.2f}%")

            position = 0

    # =========================
    # REPORT
    # =========================
    total_trades = len(trades)
    win_trades = len([t for t in trades if t > 0])
    loss_trades = len([t for t in trades if t <= 0])

    avg_profit = sum(trades) / total_trades if total_trades > 0 else 0

    print("\n📊 PROFIT BACKTEST REPORT")
    print("----------------------------")
    print(f"Trades: {total_trades}")
    print(f"Win Rate: {win_trades / total_trades * 100 if total_trades else 0:.2f}%")
    print(f"Avg Profit: {avg_profit:.2f}%")
    print(f"Final Equity: {equity:.2f}")
