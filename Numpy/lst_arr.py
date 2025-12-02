# Convert a Python list of prices into an array → apply discount.

import numpy as np

lst =[200,500,400,250,430,550,1200]
arr=np.array(lst)

# discount =10 % ,so 90% price remains.
discounted_price=arr*0.9

print(f'Original Prices : {arr}\n Discounted Prices :{discounted_price} ')
