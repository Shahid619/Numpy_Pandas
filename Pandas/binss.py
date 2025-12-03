import pandas as pd
import numpy as np

# 1. Create example data (replace this with your actual sales data Series)
sales_data = pd.Series(np.random.randint(0, 1000, size=50))
print("Original Sales Data Sample:")
print(sales_data.head())
print("-" * 30)

# 2. Define the bin edges and corresponding labels
#    Thresholds chosen here are illustrative (0-300=Low, 301-700=Medium, 701-1000=High)
bins = [0, 300, 700, 1000]
labels = ['Low', 'Medium', 'High']

# 3. Use pd.cut() to assign data points to bins
sales_groups = pd.cut(
    sales_data,
    bins=bins,
    labels=labels,
    right=False  # Makes bins left-inclusive: [0, 300), [300, 700), [700, 1000]
)

# 4. View the result and counts
print("Binned Sales Groups:")
print(sales_groups.head())
print("-" * 30)

print("Sales Group Counts:")
print(sales_groups.value_counts())
