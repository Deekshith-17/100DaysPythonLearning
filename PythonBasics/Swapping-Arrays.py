import numpy as np

# Creating a 2D array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Swapping axes 0 and 1 (rows and columns)
swapped = np.swapaxes(arr, 0, 1)

print("Original Array:")
print(arr)

print("\nArray After Swapping Axes:")
print(swapped)