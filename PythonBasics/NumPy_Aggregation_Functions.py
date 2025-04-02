import numpy as np

# Creating an array
a = np.array([[1, 2, 3], [4, 5, 6]])

# Summing elements
result = np.sum(a)
print(result)

# Summing along axis 0 (columns)
result_axis0 = np.sum(a, axis=0)
print(result_axis0)

# Summing along axis 1 (rows)
result_axis1 = np.sum(a, axis=1)
print(result_axis1)