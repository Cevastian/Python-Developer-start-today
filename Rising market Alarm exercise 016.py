# Rising market Alarm exercise 016

import pybithumb

ada = pybithumb.get_ohlcv("ADA")
close = ada["close"]

window = close.rolling(5)
ma5 = window.mean()
print(ma5)

