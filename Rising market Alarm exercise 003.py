# Rising market Alarm exercise 003

import pybithumb
import time

tickers = pybithumb.get_tickers()
print(tickers)

for ticker in tickers:
    price = pybithumb.get_current_price(ticker)
    print(ticker, price)
    time.sleep(1)
    
