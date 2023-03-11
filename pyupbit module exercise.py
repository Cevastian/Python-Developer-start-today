# pyupbit module exercise

import pyupbit
print(pyupbit.Upbit)

tickers = pyupbit.get_tickers()
print(tickers)

tickers = pyupbit.get_tickers(fiat="KRW")
print(tickers)

price = pyupbit.get_current_price("KRW-ADA")
print(price)

price = pyupbit.get_current_price("BTC-ADA")
print(price)

price = pyupbit.get_current_price(["KRW-ADA", "KRW-ETH", "USDT-BTC"])
print(price)

tickers = ["KRW-BTC", "KRW-ETH", "KRW-XRP", "KRW-ADA"]

df = pyupbit.get_ohlcv(tickers[2])
print(df)

df = pyupbit.get_ohlcv(tickers[2], interval="month", count=50)
print(df)

orderbook = pyupbit.get_orderbook("KRW-ADA")
print(orderbook)


orderbook = pyupbit.get_orderbook("KRW-ADA")
print(orderbook)
print(type(orderbook))
bids_asks = orderbook['orderbook_units']

for bid_ask in bids_asks:
    print(bid_ask)
    