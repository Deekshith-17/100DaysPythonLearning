import numpy as np

# Define two matrices
matrix1 = np.array([[1, 2],
                    [3, 4]])

matrix2 = np.array([[5, 6],
                    [7, 8]])

# Perform matrix multiplication using np.dot
result = np.dot(matrix1, matrix2)
print(result)