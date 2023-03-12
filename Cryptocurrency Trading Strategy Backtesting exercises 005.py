# Cryptocurrency Trading Strategy Backtesting exercises 005

import numpy as np
from pandas import DataFrame

data = {'Bithumb': [100, 120, 150, 180], 'Upbit': [80, 90, 170, 210]}

df = DataFrame(data)
df['Lowest Price'] = np.where(df['Bithumb'] < df['Upbit'], 'Bithumb', 'Upbit')
df.to_excel("Better cryptocurrency exchange.xlsx")
