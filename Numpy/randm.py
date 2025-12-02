# Generate random sales numbers for 30 days.
import numpy as np

rng=np.random.default_rng()

daily_sales=rng.integers(10,30,30)

print(daily_sales)
print('avg sale/day: ',daily_sales.mean())

# create a new array containing only the days where sales were above a specified target (e.g., 150 units).

# target_sales=np.array(daily_sales.any(where=daily_sales>15))
# print(target_sales.all())

