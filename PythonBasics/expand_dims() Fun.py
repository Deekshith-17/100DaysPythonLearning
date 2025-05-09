import numpy as np

# Creating a 1D NumPy array
arr = np.array([1, 2, 3, 4])

# Adding a new axis to create a 2D column vector
expanded_arr = np.expand_dims(arr, axis=1)

print("Original Array:\n", arr)
print("Array with New Axis:\n", expanded_arr)