# Restful API JSON DateTime exercise 001

import requests
import datetime

answer = requests.get("https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=ada_krw")
ada = answer.json()

timestamp = ada["timestamp"]
date = datetime.datetime.fromtimestamp(timestamp/1000)
print(date)
