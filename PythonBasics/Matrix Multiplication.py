import numpy as np

matrix_1 = np.array([[1, 2], [3, 4]])
matrix_2 = np.array([[5, 6], [7, 8]])

# Matrix multiplication using *
matrix_product1 = matrix_1 * matrix_2
print("Matrix Multiplication (*):\n", matrix_product1)

# Matrix multiplication using @
matrix_product2 = matrix_1 @ matrix_2
print("Matrix Multiplication (@):\n", matrix_product2)

# Matrix multiplication using np.dot()
matrix_product3 = np.dot(matrix_1, matrix_2)
print("Matrix Multiplication (np.dot()):\n", matrix_product3)

# Matrix multiplication using np.matmul()
matrix_product4 = np.matmul(matrix_1, matrix_2)
print("Matrix Multiplication (np.matmul()):\n", matrix_product4)