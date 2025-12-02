# Normalize data (x - min / max - min). 

import numpy as np

rng=np.random.default_rng()
random_num=rng.integers(50,size=30)

min=np.min(random_num)
max=np.max(random_num)

Normalize_data=(random_num-min/max-min)

print(f'\nNormalized data: {Normalize_data}')
print(f'\nRandom numbers list :{random_num}\n Minimum-Num :{min}\n Maximum-Num :{max}\n')

