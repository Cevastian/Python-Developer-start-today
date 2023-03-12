# Cryptocurrency Trading Strategy Backtesting exercises 006-1

import pybithumb
import numpy as np
from pandas import DataFrame

df = pybithumb.get_ohlcv("ADA")
df = df['2021']

df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = (df['open'] + df['range'].shift(1))
df['earning rate'] = np.where(df['target'] < df['high'], df['close'] / df['target'], 1)

earningrate = df['earning rate'].cumprod()[-2]
print(earningrate)
