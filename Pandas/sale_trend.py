# import pandas as pd
# import matplotlib.pyplot as plt

# # Sample data (replace with your actual data)
# data = {
#     'Date': pd.to_datetime(['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01']),
#     'Value': [10, 12, 15, 13, 18]
# }
# df = pd.DataFrame(data)
# df.set_index('Date', inplace=True)

# # Plotting the trend
# plt.figure(figsize=(10, 6))
# plt.plot(df.index, df['Value'], marker='o', linestyle='-')
# plt.title('Trend Analysis of Value Over Time')
# plt.xlabel('Date')
# plt.ylabel('Value')
# plt.grid(True)
# plt.show()

# =====================================outlier using : IQR

import pandas as pd
import numpy as np

# 1. Load the data into a DataFrame (assuming 'sales' is already cleaned and numeric)
data = {
    'order_id': ['O500', 'O501', 'O500', 'O502', 'O503', 'O504', 'O505', 'O506'],
    'sales': [1200.00, 750.00, 1200.00, 45.00, 50.00, 450.00, 99999.00, 88.00]
}
df_orders = pd.DataFrame(data)

# We focus on the 'sales' column
sales_data = df_orders['sales']

# 2. Calculate Q1 (25th percentile) and Q3 (75th percentile)
Q1 = sales_data.quantile(0.25)
Q3 = sales_data.quantile(0.75)

# 3. Calculate the Interquartile Range (IQR)
IQR = Q3 - Q1

print(f"Q1 (25th percentile): ${Q1}")
print(f"Q3 (75th percentile): ${Q3}")
print(f"IQR: ${IQR}")

# 4. Determine the Lower and Upper Fences
lower_fence = Q1 - (1.5 * IQR)
upper_fence = Q3 + (1.5 * IQR)

print(f"\nLower Fence (Outlier boundary): ${lower_fence}")
print(f"Upper Fence (Outlier boundary): ${upper_fence}")

# 5. Identify the Outliers
# A data point is an outlier if it is < lower_fence OR > upper_fence
outliers = sales_data[(sales_data < lower_fence) | (sales_data > upper_fence)]

print("\n--- Identified Outliers ---")
print(outliers)

# You can also filter the original DataFrame to see the full outlier records
outlier_records = df_orders[(df_orders['sales'] < lower_fence) | (df_orders['sales'] > upper_fence)]
print("\nOutlier Order Details:")
print(outlier_records)
