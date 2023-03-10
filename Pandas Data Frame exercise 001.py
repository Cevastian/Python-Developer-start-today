# Pandas Data Frame exercise 001

from pandas import DataFrame

data = {'open':[100, 200, 300, 400], "high":[110, 220, 330, 440]}
dtframe = DataFrame(data)

print(dtframe)

data = {"open":[737, 750, 764], "high":[755, 780, 792], "low":[700, 710, 723], "close":[750, 770, 782]}
dtFrame = DataFrame(data, index = ["2023-03-05", "2023-03-06", "2023-03-07"])

print(dtFrame)
