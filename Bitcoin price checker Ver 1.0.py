import requests
import json

current_price = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
print(current_price)
print(current_price.content)
print(current_price.json())