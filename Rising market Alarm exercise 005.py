# Rising market Alarm exercise 005

import pybithumb

orderbook = pybithumb.get_orderbook("ADA")
print(orderbook)

for k in orderbook:
    print(k)


print(orderbook['payment_currency'])

print(orderbook['order_currency'])

