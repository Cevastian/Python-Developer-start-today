# Restful API exercise 001

import requests

r = requests.get("https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=ada_krw")

print(r.text)
