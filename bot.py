import ccxt, requests, os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

EXCHANGES = {
    'binance': ccxt.binance({'enableRateLimit': True}),
    'bitget': ccxt.bitget({'enableRateLimit': True}),
    'okx': ccxt.okx({'enableRateLimit': True})
}
COINS = ['BTC/USDT:USDT','ETH/USDT:USDT','SOL/USDT:USDT','XRP/USDT:USDT','DOGE/USDT:USDT','PEPE/USDT:USDT','WIF/USDT:USDT','SHIB/USDT:USDT','BONK/USDT:USDT','AVAX/USDT:USDT']

def send(msg):
    try:
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"}, timeout=10)
    except: pass

for ex_name, ex in EXCHANGES.items():
    for coin in COINS:
        try:
            ticker = ex.fetch_ticker(coin)
            funding = ex.fetch_funding_rate(coin)['fundingRate']*100
            price = ticker['last']
            volume = ticker['quoteVolume'] or 0
            change = ticker['percentage'] or 0
            vol = f"${volume/1e9:.2f}B" if volume>=1e9 else f"${volume/1e6:.1f}M"
            sig=""
            if funding <= -0.3 and change > 1:
                sig = f"🔴 *SHORT KARO* {coin}\n💰 Price: ${price} ({change:+.2f}%)\n📦 Vol: {vol}\n📈 Fund: {funding:.4f}%"
            elif funding >= 0.3 and change < -1:
                sig = f"🟢 *LONG KARO* {coin}\n💰 Price: ${price} ({change:+.2f}%)\n📦 Vol: {vol}\n📈 Fund: {funding:.4f}%"
            if sig: send(sig)
        except: continue
