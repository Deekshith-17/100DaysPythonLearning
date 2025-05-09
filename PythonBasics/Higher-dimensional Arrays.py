import numpy as np

# Creating a 1D NumPy array
arr = np.array([1, 2, 3])

# Adding two new axes to create a 3D array
expanded_arr = np.expand_dims(arr, axis=(0, 2))

print("Original Array:\n", arr)
print("3D Array with New Axes:\n", expanded_arr)
print("Shape of 3D Array:", expanded_arr.shape)