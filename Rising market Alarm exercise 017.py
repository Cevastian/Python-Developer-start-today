# Rising market Alarm exercise 017

import pybithumb

df = pybithumb.get_ohlcv("ADA")
ma5 = df["close"].rolling(window=5).mean()
last_ma5 = ma5[-2]

price = pybithumb.get_current_price("ADA")

if price > last_ma5:
    print("Bull market")
else:
    print("Bear market")
    