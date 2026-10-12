import ccxt, requests, os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

EXCHANGES = {
    'binance': ccxt.binance({'enableRateLimit': True}),
    'bitget': ccxt.bitget({'enableRateLimit': True}),
    'okx': ccxt.okx({'enableRateLimit': True})
}
COINS = ['BTC/USDT:USDT','ETH/USDT:USDT','SOL/USDT:USDT','BNB/USDT:USDT','XRP/USDT:USDT','DOGE/USDT:USDT','ADA/USDT:USDT','AVAX/USDT:USDT','SHIB/USDT:USDT','DOT/USDT:USDT','LINK/USDT:USDT','TRX/USDT:USDT','MATIC/USDT:USDT','LTC/USDT:USDT','BCH/USDT:USDT','UNI/USDT:USDT','NEAR/USDT:USDT','PEPE/USDT:USDT','XLM/USDT:USDT','ETC/USDT:USDT','ICP/USDT:USDT','APT/USDT:USDT','STX/USDT:USDT','FIL/USDT:USDT','IMX/USDT:USDT','TAO/USDT:USDT','ARB/USDT:USDT','HBAR/USDT:USDT','INJ/USDT:USDT','MKR/USDT:USDT','VET/USDT:USDT','RNDR/USDT:USDT','GRT/USDT:USDT','ATOM/USDT:USDT','LDO/USDT:USDT','OP/USDT:USDT','AAVE/USDT:USDT','QNT/USDT:USDT','XMR/USDT:USDT','FLOW/USDT:USDT','EGLD/USDT:USDT','SAND/USDT:USDT','MANA/USDT:USDT','AXS/USDT:USDT','ALGO/USDT:USDT','THETA/USDT:USDT','FTM/USDT:USDT','RUNE/USDT:USDT','CHZ/USDT:USDT','KAVA/USDT:USDT','XTZ/USDT:USDT','EOS/USDT:USDT','NEO/USDT:USDT','KLAY/USDT:USDT','CAKE/USDT:USDT','ROSE/USDT:USDT','ONE/USDT:USDT','GALA/USDT:USDT','IOTA/USDT:USDT','CFX/USDT:USDT','BLUR/USDT:USDT','JASMY/USDT:USDT','WIF/USDT:USDT','BONK/USDT:USDT','FLOKI/USDT:USDT','BOME/USDT:USDT','MEME/USDT:USDT','PYTH/USDT:USDT','JUP/USDT:USDT','STRK/USDT:USDT','W/USDT:USDT','ENA/USDT:USDT','ETHFI/USDT:USDT','WLD/USDT:USDT','SEI/USDT:USDT','SUI/USDT:USDT','TIA/USDT:USDT','ORDI/USDT:USDT','1000SATS/USDT:USDT','AR/USDT:USDT','FET/USDT:USDT','DYDX/USDT:USDT','GMT/USDT:USDT','APE/USDT:USDT','LRC/USDT:USDT','ENJ/USDT:USDT','ZIL/USDT:USDT','BAT/USDT:USDT','COMP/USDT:USDT','ZEC/USDT:USDT','DASH/USDT:USDT','WAVES/USDT:USDT','MINA/USDT:USDT','KSM/USDT:USDT','CRV/USDT:USDT','1INCH/USDT:USDT','SNX/USDT:USDT','ENS/USDT:USDT','FXS/USDT:USDT','GMX/USDT:USDT','MAGIC/USDT:USDT','ID/USDT:USDT','RDNT/USDT:USDT','EDU/USDT:USDT','MAV/USDT:USDT','PENDLE/USDT:USDT','ARKM/USDT:USDT','AGLD/USDT:USDT','YGG/USDT:USDT','LPT/USDT:USDT','GLM/USDT:USDT','ONT/USDT:USDT','QTUM/USDT:USDT','WAXP/USDT:USDT','IOST/USDT:USDT','SKL/USDT:USDT','CTSI/USDT:USDT','CELO/USDT:USDT','HIGH/USDT:USDT','BIGTIME/USDT:USDT','TOKEN/USDT:USDT','LEVER/USDT:USDT','XVS/USDT:USDT','OM/USDT:USDT','NTRN/USDT:USDT','SFP/USDT:USDT','LOOM/USDT:USDT','ASTR/USDT:USDT','KDA/USDT:USDT','FLUX/USDT:USDT','BAND/USDT:USDT','TRB/USDT:USDT','ARK/USDT:USDT','COTI/USDT:USDT','LQTY/USDT:USDT','STORJ/USDT:USDT','API3/USDT:USDT','TWT/USDT:USDT','SUSHI/USDT:USDT','ZRX/USDT:USDT','DENT/USDT:USDT','HOT/USDT:USDT','WIN/USDT:USDT','BTT/USDT:USDT','JST/USDT:USDT','SUN/USDT:USDT','OMG/USDT:USDT','ICX/USDT:USDT','DGB/USDT:USDT','SC/USDT:USDT','RVN/USDT:USDT','CKB/USDT:USDT','NKN/USDT:USDT','AUDIO/USDT:USDT','BICO/USDT:USDT','BEL/USDT:USDT','ALICE/USDT:USDT','TLM/USDT:USDT','CHESS/USDT:USDT','QI/USDT:USDT','PORTO/USDT:USDT','BAR/USDT:USDT','CITY/USDT:USDT','LAZIO/USDT:USDT','OG/USDT:USDT','ATM/USDT:USDT','JUV/USDT:USDT','PSG/USDT:USDT','SANTOS/USDT:USDT','ALPINE/USDT:USDT','LINA/USDT:USDT','PEOPLE/USDT:USDT','LUNC/USDT:USDT','USTC/USDT:USDT','LUNA/USDT:USDT','NOT/USDT:USDT','DOGS/USDT:USDT','TON/USDT:USDT','TURBO/USDT:USDT','TRUMP/USDT:USDT','PNUT/USDT:USDT','GOAT/USDT:USDT','POPCAT/USDT:USDT','MEW/USDT:USDT','BRETT/USDT:USDT','MOG/USDT:USDT','CAT/USDT:USDT','NEIRO/USDT:USDT','ACT/USDT:USDT','FTT/USDT:USDT','AGIX/USDT:USDT','OCEAN/USDT:USDT','ROSE/USDT:USDT','FLM/USDT:USDT','POLYX/USDT:USDT','MBOX/USDT:USDT','MDX/USDT:USDT','MDT/USDT:USDT','MOVR/USDT:USDT','OXT/USDT:USDT','PUNDIX/USDT:USDT','QKC/USDT:USDT','RIF/USDT:USDT','SLP/USDT:USDT','SUPER/USDT:USDT','SXP/USDT:USDT','TOMO/USDT:USDT','TRU/USDT:USDT','UTK/USDT:USDT','WING/USDT:USDT','XEM/USDT:USDT','YFII/USDT:USDT','ZKS/USDT:USDT','BAL/USDT:USDT','BNT/USDT:USDT','CELR/USDT:USDT','CHR/USDT:USDT','CVC/USDT:USDT','DNT/USDT:USDT','DOCK/USDT:USDT','ELF/USDT:USDT','FUN/USDT:USDT','GAS/USDT:USDT','GNO/USDT:USDT','HARD/USDT:USDT','HNT/USDT:USDT','KMD/USDT:USDT','LIT/USDT:USDT','LSK/USDT:USDT','MTL/USDT:USDT','NANO/USDT:USDT','NAV/USDT:USDT','OCEAN/USDT:USDT','OGN/USDT:USDT','PAXG/USDT:USDT','PERL/USDT:USDT','PERP/USDT:USDT','PHB/USDT:USDT','PNT/USDT:USDT','POLS/USDT:USDT','POWR/USDT:USDT','QSP/USDT:USDT','RAMP/USDT:USDT','REEF/USDT:USDT','REN/USDT:USDT','RLC/USDT:USDT','RSR/USDT:USDT','SKY/USDT:USDT','STX/USDT:USDT','SYS/USDT:USDT','TFUEL/USDT:USDT','UNFI/USDT:USDT','VTHO/USDT:USDT','WABI/USDT:USDT','WAN/USDT:USDT','WTC/USDT:USDT','XVG/USDT:USDT','YFI/USDT:USDT','ZEN/USDT:USDT','KISHU/USDT:USDT','ELON/USDT:USDT','SAITAMA/USDT:USDT','AKITA/USDT:USDT','VOLT/USDT:USDT','HAMSTER/USDT:USDT','CATI/USDT:USDT','BABYDOGE/USDT:USDT']

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

PUMP_LIMIT = 25.0
MIN_VOL_M = 10.0
SHORT_FUND = -0.0020
LONG_FUND = 0.0020
last_signal = {}

def get_rsi(p):
    s=pd.Series(p); d=s.diff()
    g=d.where(d>0,0).rolling(14).mean()
    l=-d.where(d<0,0).rolling(14).mean()
    rs=g/l; rsi=100-(100/(1+rs))
    return float(rsi.iloc[-1])

def send(msg):
    try: requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": msg}, timeout=10)
    except: pass

for ex_name, ex in EXCHANGES.items():
    for coin in COINS:
        try:
            t=ex.fetch_ticker(coin)
            price=t['last']; change=t['percentage']
            if price is None or change is None: continue
            qvol=t.get('quoteVolume') or 0; bvol=t.get('baseVolume') or 0
            vol=qvol if qvol>0 else bvol*price
            vol_m=vol/1_000_000
            fund=float(ex.fetch_funding_rate(coin)['fundingRate'])
            if vol_m < MIN_VOL_M: continue
            if abs(change) > PUMP_LIMIT: continue
            if coin in last_signal and time.time()-last_signal[coin]<3600: continue
            ohlcv=ex.fetch_ohlcv(coin,'1m',limit=100)
            closes=[c[4] for c in ohlcv]; rsi=get_rsi(closes)
            side=None
            if fund<=SHORT_FUND and rsi<70: side="SHORT"
            elif fund>=LONG_FUND and rsi>30: side="LONG"
            if not side: continue
            last_signal[coin]=time.time()
            color="🔴" if side=="SHORT" else "🟢"
            msg=f"{color} {side} KARO {coin}\n💰 Price: ${price} ({change:.2f}%)\n📦 Vol: ${vol_m:.1f}M\n📈 Fund: {fund*100:.4f}%\n📊 RSI: {rsi:.1f}\n🏦 Ex: {ex_name}"
            send(msg)
            print(msg)
        except Exception as e:
            print(f"Err {coin}: {e}")
        time.sleep(0.3)
            change = ticker['percentage'] or 0
            vol = f"${volume/1e9:.2f}B" if volume>=1e9 else f"${volume/1e6:.1f}M"
            sig=""
            if funding <= -0.3 and change > 1:
                sig = f"🔴 *SHORT KARO* {coin}\n💰 Price: ${price} ({change:+.2f}%)\n📦 Vol: {vol}\n📈 Fund: {funding:.4f}%"
            elif funding >= 0.3 and change < -1:
                sig = f"🟢 *LONG KARO* {coin}\n💰 Price: ${price} ({change:+.2f}%)\n📦 Vol: {vol}\n📈 Fund: {funding:.4f}%"
            if sig: send(sig)
        except: continue
