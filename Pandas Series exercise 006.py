# Pandas Series calculation with compare with Python List

my_list = [100, 200, 300, 400]
# print(my_list / 10)

new_list = []
for val in my_list:
    new_list.append( val / 2.5)
    
print(new_list)

from pandas import Series
srs = Series([100, 200, 300, 400])
print(srs / 5)
print(srs * 2)
print(srs)