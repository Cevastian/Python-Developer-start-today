# Pandas Series exercise 002

from pandas import Series

date = ['2023-03-05', '2023-03-06', '2023-03-07', '2023-03-08', '2023-03-09']
ada_close = [478, 483, 492, 454, 427]

srs = Series(ada_close, index=date)
# srs = Series(ada_close)
print(srs)
print(type(srs))

print(srs[0])
print(srs['2023-03-07'])