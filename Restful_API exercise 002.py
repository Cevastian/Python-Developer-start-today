# Restful API JSON exercise 001

import requests

answer = requests.get("https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=ada_krw")

print(answer.text)


ada = answer.json()
print(ada)
print(type(ada))

print(ada['last'])
print(ada['high'])
print(ada['low'])
print(ada['bid'])
print(ada['ask'])
print(ada['volume'])