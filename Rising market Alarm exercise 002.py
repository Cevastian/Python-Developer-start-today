# Rising market Alarm exercise 002 

import pybithumb
import time

# Get current price of cryptocurrency every 1 second
while True:
    price = pybithumb.get_current_price("ADA")
    print(price)
    time.sleep(1)