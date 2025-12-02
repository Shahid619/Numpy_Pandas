# Create 3×3 matrices → add, multiply, transpose.

import numpy as np

rng=np.random.default_rng()
matrix=rng.integers(10,size=(3,3))

# print(matrix)
add_mat=matrix + 2
mul_mat=matrix * 2
trans_mat =matrix.transpose()

print(f'\nOriginal Matrix :{matrix}\n addition of matrix :{add_mat}\n Multiply matrix :{mul_mat}\n transpose of matrix :{trans_mat}')