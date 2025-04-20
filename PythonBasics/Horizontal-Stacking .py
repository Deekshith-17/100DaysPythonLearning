import numpy as np

# Create two 2D arrays
array1 = np.array([[1, 2, 3],
                   [4, 5, 6]])
array2 = np.array([[7, 8, 9],
                   [10, 11, 12]])

# Horizontally stack the arrays
hstacked_array = np.hstack((array1, array2))

print("Horizontally Stacked 2D Array:\n", hstacked_array)