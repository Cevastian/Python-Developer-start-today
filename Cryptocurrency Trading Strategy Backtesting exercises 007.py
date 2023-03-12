# Cryptocurrency Trading Strategy Backtesting exercises 007

import pyupbit
import numpy as np
from pandas import DataFrame

df = pyupbit.get_ohlcv("KRW-BTC")
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)

fee = 0.0032

df['ror'] = np.where(df['high'] > df['target'], df['close'] / df['target'] - fee, 1)

ror = df['ror'].cumprod()[-2]
print(ror)

