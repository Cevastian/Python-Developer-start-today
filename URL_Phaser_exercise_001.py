# URL phaser exercise 001

import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code=0660"
html = requests.get(url).text

print(html)
