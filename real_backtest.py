from analyzer import analyze
from data_provider import get_real_market_history


def run():

    prices = get_real_market_history(30)

    print("\n📊 REAL MARKET BACKTEST (TSETMC BASED)")
    print("━━━━━━━━━━━━━━━━━━━━━━")

    position = 0
    entry = 0
    trades = []
    equity = 100

    for i in range(20, len(prices)):

        window = prices[i-20:i]

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

        print(f"Day {i-19} | Price {price} | Score {result['scores']['total_score']} | Signal {signal}")

        if signal in ["BUY", "STRONG_BUY"] and position == 0:
            position = 1
            entry = price

        elif signal in ["RISK", "NO_TRADE"] and position == 1:

            profit = ((price - entry) / entry) * 100
            equity += equity * (profit / 100)

            trades.append(profit)
            print(f"SELL → PnL: {profit:.2f}%")

            position = 0

    print("\n━━━━━━━━━━━━━━━━━━━━━━")
    print("TRADES:", len(trades))
    print("WIN RATE:", len([t for t in trades if t > 0]) / len(trades) * 100 if trades else 0)
    print("AVG PROFIT:", sum(trades) / len(trades) if trades else 0)
    print("FINAL EQUITY:", equity)
