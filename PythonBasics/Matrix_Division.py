import numpy as np

# Creating a matrix
A = np.array([[1, 2], [3, 4]])

# Creating another matrix
B = np.array([[2, 0], [1, 3]])

# Solving the matrix division A/B
# Equivalent to A * B^-1
result = np.dot(A, np.linalg.inv(B))
print(result)