# Pandas DataFrame API call exercise 

import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/sise_day.nhn?code=066570"
res = requests.get(url, headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})

df = pd.read_html(res.text)

print(df)
print(df[0].dropna(axis=0))
#print(df[0].dropna(axis=1))

# For Pandas Dataframe error exercise, please refer following codes 

import pandas as pd
import requests
url_link = 'https://finance.yahoo.com/quote/NFLX/history?p=NFLX%27'
r = requests.get(url_link,headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
read_html_pandas_data = pd.read_html(r.text)[0]
print(read_html_pandas_data.dropna(axis=0))