# Cryptocurrency Trading Strategy Backtesting exercises 006

import pyupbit
import numpy as np
from pandas import DataFrame

df = pyupbit.get_ohlcv("KRW-ADA")
df['range'] = (df['high'] - df['low']) * 3
df['target'] = (df['open'] + df['range'].shift(1))

df['ror'] = np.where(df['high'] > df['target'], df['close'] / df['target'], 1)
ror = df['ror'].cumprod()[-2]
print(type(ror))
print(ror)

df.to_excel("Cryptocurrency trading result(XRP).xlsx")
