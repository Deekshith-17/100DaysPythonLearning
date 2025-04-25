import numpy as np

# Define multiple 1D arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([2, 3, 4])
arr3 = np.array([4, 5, 6])

# Compute the union of three arrays
# Union of first two arrays
union_temp = np.union1d(arr1, arr2)  
# Union with the third array
union_result = np.union1d(union_temp, arr3) 

print("Union of multiple arrays (sequential):", union_result)