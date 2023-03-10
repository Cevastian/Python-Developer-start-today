# Rising market Alarm exercise 015

import pybithumb

ada = pybithumb.get_ohlcv("ADA")
close = ada["close"]

print((close[0] + close[1] + close[2] + close[3] + close[4]) / 5)
print((close[1] + close[2] + close[3] + close[4] + close[5]) / 5)
print((close[2] + close[3] + close[4] + close[5] + close[6]) / 5)
