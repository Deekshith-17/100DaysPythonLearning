import numpy as np

# Creating a 2D NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Swapping the first and last columns
arr[:, [0, 2]] = arr[:, [2, 0]]

print("Array after swapping columns:")
print(arr)