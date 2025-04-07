import numpy as np

# Creating two 2D arrays
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Element-wise multiplication
element_wise_result = a * b
print("Element-wise multiplication:\n", element_wise_result)

# Matrix multiplication
matrix_result = np.dot(a, b)
print("Matrix multiplication:\n", matrix_result)