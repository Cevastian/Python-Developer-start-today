# Cryptocurrency Trading Strategy Backtesting exercises 001

import pyupbit

df = pyupbit.get_ohlcv("KRW-ADA")
print(df.tail())
