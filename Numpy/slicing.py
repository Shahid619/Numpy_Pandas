# Create a 4x5 NumPy array representing monthly sales for 4 different regions over 5 months. Extract sales data for only the first two regions and only the last three months.

import numpy as np 

rng = np.random.default_rng()
matrix=rng.integers(500,1000,size=(4,5))


# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[1, 1:4])

extract_sub_set=matrix[0:2,2:]
# print(matrix)

print(matrix) 
print(f'1st 2 regions ,lst 3 months data :\n{extract_sub_set}\n')