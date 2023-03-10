# Rising market Alarm exercise 014

import pybithumb

ada = pybithumb.get_ohlcv("ADA")
print(ada)

close = ada['close']
print(close)