# Pandas Dataframe value shift exercise

from pandas import DataFrame

data = {"open":[737,750, 743, 745, 767], "high":[755, 780, 779, 764, 759], "low":[700, 710, 715, 722, 714], "close":[750, 770, 745, 753, 738]}
df = DataFrame(data)
print(df)

# Dataframe shift exercise
df1 = df.shift(periods=2, fill_value=100)
print(df1)

df2 = df.shift(periods=1, axis="rows", fill_value=0)
print(df2)

