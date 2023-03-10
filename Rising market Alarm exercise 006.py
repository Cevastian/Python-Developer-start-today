# Rising market Alarm exercise 006

import pybithumb
import datetime

orderbook = pybithumb.get_orderbook("ADA")
ms = int(orderbook["timestamp"])

dt = datetime.datetime.fromtimestamp(ms/1000)
print(dt)
