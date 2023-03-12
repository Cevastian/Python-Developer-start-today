# Cryptocurrency Trading Strategy Backtesting exercises 009

import numpy as np
import pyupbit
from pandas import DataFrame

df = pyupbit.get_ohlcv('KRW-ADA')

df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)

fee = 0.0032

df['ror'] = np.where(df['high'] > df['target'], df['close'] / df['target'], 1)

ror = df['ror'].cumprod()[-2]
print(ror)

df['hpr'] = df['ror'].cumprod()
df.to_excel("Cryptocurrency trading ROR result(ADA).xlsx")
