# Pandas Dataframe practice 001

import pandas as pd

data = {"open":[737, 750, 770], "high":[755, 780, 770], "low":[700, 710, 750], "close":[750, 770, 730]}
date_list = ["2018-01-01", "2018-01-02", "2018-01-03"]
df = pd.DataFrame(data, index=date_list)
print(df)

volt = df["high"] - df["low"]
df["volatility"] = volt
print(df)