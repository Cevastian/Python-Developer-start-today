# Rising market Alarm exercise 008

import pybithumb

orderbook = pybithumb.get_orderbook("ADA")
bids = orderbook["bids"]

for bid in bids:
    price = bid['price']
    quant = bid['quantity']
    print("Bid order price: ", price, "Bid order quantity: ", quant)
    
    
asks = orderbook["asks"]

for ask in asks:
    price = ask['price']
    quant = ask['quantity']
    print("Ask order price: ", price,", " "Ask order quantity: ", quant)
    