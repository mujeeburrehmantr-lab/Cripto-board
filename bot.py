import ccxt, requests, os, time
import pandas as pd

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def get_rsi(prices):
    s = pd.Series(prices)
    d = s.diff()
    g = d.where(d>0,0).rolling(14).mean()
    l = -d.where(d<0,0).rolling(14).mean()
    rs = g/l
    return float((100-(100/(1+rs))).iloc[-1])

def send(msg):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": msg}, timeout=10)
    except:
        pass

exchanges = {
    "binance": ccxt.binance({"enableRateLimit": True}),
    "bitget": ccxt.bitget({"enableRateLimit": True}),
    "okx": ccxt.okx({"enableRateLimit": True})
}

coins = ["BTC/USDT:USDT","ETH/USDT:USDT","SOL/USDT:USDT","MAGIC/USDT:USDT"]

last_time = {}

for name, ex in exchanges.items():
    for coin in coins:
        try:
            tk = ex.fetch_ticker(coin)
            price = tk.get("last")
            chg = tk.get("percentage")
            if not price or chg is None:
                continue
            qv = tk.get("quoteVolume") or 0
            bv = tk.get("baseVolume") or 0
            vol_m = (qv if qv>0 else bv*price)/1000000
            if vol_m < 10:
                continue
            if abs(chg) > 25:
                continue
            fr = float(ex.fetch_funding_rate(coin)["fundingRate"])
            ohlcv = ex.fetch_ohlcv(coin, "1m", limit=100)
            rsi = get_rsi([c[4] for c in ohlcv])
            if coin in last_time and time.time()-last_time[coin] < 3600:
                continue
            side = None
            if fr <= -0.002 and rsi < 70:
                side = "SHORT"
            elif fr >= 0.002 and rsi > 30:
                side = "LONG"
            if not side:
                continue
            last_time[coin] = time.time()
            emoji = "🔴" if side=="SHORT" else "🟢"
            txt = f"{emoji} {side} KARO {coin}\n💰 Price: ${price} ({chg:.2f}%)\n📦 Vol: ${vol_m:.1f}M\n📈 Fund: {fr*100:.4f}%\n📊 RSI: {rsi:.1f}\n🏦 Ex: {name}"
            send(txt)
        except:
            continue
