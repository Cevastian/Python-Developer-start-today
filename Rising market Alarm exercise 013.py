# Rising market Alarm exercise 013

import pybithumb
import time

while True:
    price = pybithumb.get_current_price("ADA")
    
    # if price is not None:
    #    print(price/10)
    # time.sleep(0.2)
    try:
        print(price/10)
    except:
        print("An error occurred", price)
    time.sleep(0.5)
    
    
    