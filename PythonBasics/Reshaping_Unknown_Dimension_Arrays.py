import numpy as np

# Original 1-D array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Reshape to 3-D array with one unknown dimension
reshaped_arr = arr.reshape((2, 2, -1))
print("Reshaped Array with Unknown Dimension:")
print(reshaped_arr)