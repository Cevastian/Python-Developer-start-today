# Pandas DataFrame with Excel file exercise 002

import pandas as pd
# dtframe = pd.read_excel("C:\\Users\\chois\\Desktop\\PythonProject\\Codes\\Coding Exercise with Cryptocurrency Auto Trading\\Pandas_DataFrame exercise 001.xlsx")
# print(dtframe)

dtframe = pd.read_excel("C:\\Data\\Pandas_DataFrame exercise 001.xlsx")
print(dtframe)

print(type(dtframe))

dtframe = dtframe.set_index('Date')
print(dtframe)

dtframe.to_excel('C:\\Data\Pandas_DataFrame exercise 001-1.xlsx')
