import ccxt, time, requests, datetime

TELEGRAM_TOKEN = "APNA_TOKEN_YAHAN_DALEIN"
CHAT_ID = "APNA_CHAT_ID_YAHAN_DALEIN"

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

print("Board Started - Price + Volume")

for ex_name, ex in EXCHANGES.items():
    for coin in COINS:
        try:
            ticker = ex.fetch_ticker(coin)
            funding = ex.fetch_funding_rate(coin)['fundingRate']*100
            oi = ex.fetch_open_interest(coin)['openInterestAmount']
            
            price = ticker['last']
            volume = ticker['quoteVolume']
            change_24h = ticker['percentage'] if ticker['percentage'] else 0
            
            # Volume ko readable banao
            vol_str = f"${volume/1e9:.2f}B" if volume>=1e9 else f"${volume/1e6:.1f}M"
            
            signal = ""
            if funding <= -0.3 and change_24h > 1:
                signal = f"🔴 *ABHI SHORT KARO - GIRNE WALA*\n🪙 Coin: {coin} ({ex_name})\n💰 Price: ${price} ({change_24h:+.2f}%)\n📦 Volume: {vol_str}\n📈 Funding: {funding:.4f}%\n📊 OI: {oi}"
            elif funding >= 0.3 and change_24h < -1:
                signal = f"🟢 *ABHI LONG KARO - UPAR JAYEGA*\n🪙 Coin: {coin} ({ex_name})\n💰 Price: ${price} ({change_24h:+.2f}%)\n📦 Volume: {vol_str}\n📈 Funding: {funding:.4f}%\n📊 OI: {oi}"
            
            if signal:
                send(signal)
                print(signal)
        except:
            continue
