import numpy as np

# Creating two 1D arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Adding new axes to create 2D row vectors
arr1_expanded = arr1[np.newaxis, :]
arr2_expanded = arr2[np.newaxis, :]

# Concatenating the row vectors along axis 0
combined_arr = np.concatenate([arr1_expanded, arr2_expanded], axis=0)

print("Array 1 with New Axis:\n", arr1_expanded)
print("Array 2 with New Axis:\n", arr2_expanded)
print("Combined Array:\n", combined_arr)