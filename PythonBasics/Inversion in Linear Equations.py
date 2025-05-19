import numpy as np

# Coefficient matrix
A = np.array([[1, 2], [3, 4]])

# Constant vector
B = np.array([[5], [6]])

# Compute the inverse of A
A_inv = np.linalg.inv(A)

# Solve for X
X = np.dot(A_inv, B)
print(X)