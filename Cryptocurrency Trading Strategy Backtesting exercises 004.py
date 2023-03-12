# Cryptocurrency Trading Strategy Backtesting exercises 004

import pyupbit
from pandas import DataFrame

df = pyupbit.get_ohlcv("KRW-ADA")
df['range'] = ((df['high'] - df['low']) * 0.5)
df['range_shift1'] = df['range'].shift(1)
df['target'] = df['open'] + df['range'].shift(1)
df.to_excel("Cryptocurrency Volatility Breakout strategy 002.xlsx")