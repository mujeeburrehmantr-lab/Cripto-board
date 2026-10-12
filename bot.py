import ccxt, requests, os, time

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send(msg):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": msg}, timeout=10)
    except:
        pass

def rsi(prices):
    gains = 0
    losses = 0
    for i in range(1, 15):
        diff = prices[-i] - prices[-i-1]
        if diff > 0:
            gains += diff
        else:
            losses -= diff
    if losses == 0:
        return 100
    rs = gains / losses
    return 100 - (100 / (1 + rs))

exchanges = {
    "binance": ccxt.binance({"enableRateLimit": True}),
    "bitget": ccxt.bitget({"enableRateLimit": True})
}

coins = ["BTC/USDT:USDT","ETH/USDT:USDT","SOL/USDT:USDT"]

for name, ex in exchanges.items():
    for coin in coins:
        try:
            t = ex.fetch_ticker(coin)
            price = t["last"]
            change = t["percentage"] or 0
            if not price: continue
            if abs(change) > 25: continue

            qv = t.get("quoteVolume") or 0
            bv = t.get("baseVolume") or 0
            vol = (qv if qv>0 else bv*price) / 1000000
            if vol < 10: continue

            f = ex.fetch_funding_rate(coin)
            funding = float(f["fundingRate"])
            ohlcv = ex.fetch_ohlcv(coin, "1m", limit=30)
            closes = [c[4] for c in ohlcv]
            r = rsi(closes)

            sig = None
            if funding <= -0.002 and r < 70: sig = "SHORT"
            if funding >= 0.002 and r > 30: sig = "LONG"
            if not sig: continue

            icon = "🔴" if sig=="SHORT" else "🟢"
            txt = f"{icon} {sig} KARO {coin} ({name})\nPrice ${price} ({change:.2f}%)\nVol ${vol:.1f}M\nFund {funding*100:.4f}%\nRSI {r:.1f}"
            send(txt)
        except:
            continue
