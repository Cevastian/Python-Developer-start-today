# Pandas Dataframe indexing & slicing exercise
from pandas import DataFrame

data = {"open" : [730, 750], "high":[755,780], "low":[700, 710], "close":[750, 770]}
df = DataFrame(data, index=["2023-03-09", "2023-03-10"])
print(df["open"])
print(df.loc["2023-03-09"])
print(df.iloc[1])

target = ["2023-03-09", "2023-03-10"]
print(df.loc[target])

target = [1]
print(df.iloc[target])
