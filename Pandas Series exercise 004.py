# Pandas Series exercise 004

from pandas import Series

date = ['2023-03-05', '2023-03-06', '2023-03-07', '2023-03-08', '2023-03-09',]
ada_close = [478, 465, 457, 443, 432]
srs = Series(ada_close, index=date)

print(srs['2023-03-05':'2023-03-07'])

print(srs[0:2])