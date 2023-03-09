# Pandas Series exercise 003

from pandas import Series

date = ['2023-03-05','2023-03-06','2023-03-07','2023-03-08','2023-03-09',]
ada_close = [478, 462, 453, 447, 438]

srs = Series(ada_close, index = date)

print(srs.index)
print(srs.values)
print(type(srs))

print(srs[['2023-03-06', '2023-03-08']])
print(srs[['2023-03-08']])