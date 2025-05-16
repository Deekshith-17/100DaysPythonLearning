import numpy as np
A = np.array([[1, 2], [3, 4]])

# Performing SVD
U, S, V = np.linalg.svd(A)
print("U matrix:\n", U)
print("Sigma values:", S)
print("V matrix:\n", V)