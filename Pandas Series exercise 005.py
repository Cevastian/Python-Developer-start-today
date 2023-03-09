# Pandas Series adding & removing value exercise

from pandas import Series

date = ['2023-03-05', '2023-03-06', '2023-03-07', '2023-03-08', '2023-03-09',]
ada_close = [465, 453, 448, 435, 428]

srs = Series(ada_close, index=date)

srs['2023-03-10'] = 419

print(srs.drop('2023-03-05'))
print(srs)