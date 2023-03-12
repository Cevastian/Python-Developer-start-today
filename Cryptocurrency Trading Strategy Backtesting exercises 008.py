# Cryptocurrency Trading Strategy Backtesting exercises 008

import pyupbit
import numpy as np
from pandas import DataFrame

fee = 0.0032

def cal_ror(k=0.5):
    df = pyupbit.get_ohlcv("KRW-ADA")
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)
    
    fee = 0.0032
    df['ror'] = np.where(df['high'] > df['target'], df['close'] / df['target'] - fee, 1)

    ror = df['ror'].cumprod()[-2]
    return ror

for k in np.arange(0.1, 1.0, 0.1):
    ror = cal_ror(k)
    print("%.1f %f" % (k, ror))
