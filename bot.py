import ccxt, requests, os, time
import pandas as pd

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

EXCHANGES = {
    'binance': ccxt.binance({'enableRateLimit': True}),
    'bitget': ccxt.bitget({'enableRateLimit': True}),
    'okx': ccxt.okx({'enableRateLimit': True})
}

COINS = ['BTC/USDT:USDT','ETH/USDT:USDT','SOL/USDT:USDT','MAGIC/USDT:USDT','RSR/USDT:USDT']

def get_rsi(prices):
    s = pd.Series(prices)
    d = s.diff()
    g = d.where(d>0,0).rolling(14).mean()
    l = -d.where(d<0,0).rolling(14).mean()
    rs = g/l
    return float((100-(100/(1+rs))).iloc[-1])

def send(m):
    try:
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", data={"chat_id":CHAT_ID,"text":m}, timeout=10)
    except: pass

last = {}

for en, ex in EXCHANGES.items():
    for coin in COINS:
        try:
            tk = ex.fetch_ticker(coin)
            price = tk['last']
            chg = tk['percentage']
            if not price or not chg: continue
            
            qv = tk.get('quoteVolume') or 0
            bv = tk.get('baseVolume') or 0
            vol_m = (qv if qv>0 else bv*price) / 1_000_000
            
            # --- BLOCK FILTERS ---
            if vol_m < 10: continue
            if abs(chg) > 25: continue
            
            fr = float(ex.fetch_funding_rate(coin)['fundingRate'])
            ohlcv = ex.fetch_ohlcv(coin,'1m',limit=100)
            rsi = get_rsi([c[4] for c in ohlcv])
            
            if coin in last and time.time()-last[coin]<3600: continue
            
            side=None
            if fr <= -0.002 and rsi < 70: side="SHORT"
            elif fr >= 0.002 and rsi > 30: side="LONG"
            if not side: continue
            
            last[coin]=time.time()
            col="🔴" if side=="SHORT" else "🟢"
            send(f"{col} {side} KARO {coin}\n💰 Price: ${price} ({chg:.2f}%)\n📦 Vol: ${vol_m:.1f}M\n📈 Fund: {fr*100:.4f}%\n📊 RSI: {rsi:.1f}\n🏦 Ex: {en}")
            time.sleep(0.3)
        except: continue
