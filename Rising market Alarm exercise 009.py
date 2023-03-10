# Rising market Alarm exercise 009

import pybithumb

all = pybithumb.get_current_price("All")

print type(all)

#for k, v in all.items():
#    print(k, v)