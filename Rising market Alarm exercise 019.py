# Rising market Alarm exercise 019

import pybithumb

def bull_market(ticker):
    df = pybithumb.get_ohlcv(ticker)
    ma5 = df['close'].rolling(window=5).mean()
    last_ma5 = ma5[-2]
    price = pybithumb.get_current_price(ticker)
    
    if price > last_ma5:
        return True
    else:
        return False
    
tickers = pybithumb.get_tickers()

for ticker in tickers:
    is_bull = bull_market(ticker)
    if is_bull:
        print(ticker, " Bull market")
    else:
        print(ticker, " Bear market")