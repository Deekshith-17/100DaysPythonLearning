import numpy as np

# Define multiple 1D arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([2, 3, 4])
arr3 = np.array([4, 5, 6])

# Concatenate all arrays into one
concatenated_array = np.concatenate((arr1, arr2, arr3))

# Find unique elements
union_result = np.unique(concatenated_array)

print("Union of multiple arrays (concatenate and unique):", union_result)