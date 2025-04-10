import numpy as np

# Creating arrays with incompatible shapes
a = np.array([1, 2, 3])
b = np.array([[1, 2], [3, 4]])

# Attempting to divide incompatible arrays
result = a / b
print(result)