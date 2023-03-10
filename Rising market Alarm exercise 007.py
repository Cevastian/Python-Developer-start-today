# Rising market Alarm exercise 007

import pybithumb

orderbook = pybithumb.get_orderbook("ADA")
bids = orderbook["bids"]
asks = orderbook["asks"]

print(bids)
print(asks)

for bid in bids:
    print(bid)
    
print(type(bids))