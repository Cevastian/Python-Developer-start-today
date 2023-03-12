# Cryptocurrency Trading Strategy Backtesting exercises 003

import pyupbit
from pandas import DataFrame

df = pyupbit.get_ohlcv("KRW-ADA")
df['range'] = (df['high'] - df['low']) * 0.5
df.to_excel("Cryptocurrency Volatility Breakout strategy 001.xlsx")
