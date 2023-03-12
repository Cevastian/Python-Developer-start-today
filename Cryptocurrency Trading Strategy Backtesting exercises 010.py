# Cryptocurrency Trading Strategy Backtesting exercises 010

import pyupbit
import numpy as np

df = pyupbit.get_ohlcv("KRW-ADA")
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)

fee = 0.0032

df['ror'] = np.where(df['high'] > df['target'], df['close'] / df['target'] - fee, 1)

df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

print("MOD(%): ", df['dd'].max())

df.to_excel("Cryptocurrency trading MDD result(ADA).xlsx")
