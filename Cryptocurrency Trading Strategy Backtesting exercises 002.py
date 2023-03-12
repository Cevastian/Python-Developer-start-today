# Cryptocurrency Trading Strategy Backtesting exercises 001

import pyupbit
from pandas import DataFrame

df = pyupbit.get_ohlcv("KRW-ADA")
df.to_excel("KRW-ADA OHLCV Backdata 001.xlsx")