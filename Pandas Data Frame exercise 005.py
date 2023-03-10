# Pandas Dataframe adding & removing values
from pandas import DataFrame
from pandas import Series

data = {"open" : [737,750], "high":[755, 780], "low":[700, 710], "close":[750, 770]}
df = DataFrame(data)

# Adding Series values in Dataframe column
srs = Series([300, 400, 500])
df["volume"] = srs

# Adding List values in Dataframe column
df["average"] = [747, 787]
print(df)

# Adding List values in Dataframe row
df.loc[2] = [100, 200, 300, 400, 500, 600]
print(df)

# Adding calculated values in Dataframe column
upper = df["open"] * 1.3
df["up 130%"] = upper
print(df)