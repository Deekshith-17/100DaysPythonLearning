import numpy as np

# Creating a 3D NumPy array
arr = np.array([[[1, 2, 3], [4, 5, 6]], 
                [[7, 8, 9], [10, 11, 12]]])

# Swapping axes 1 and 2
arr_swapped = np.swapaxes(arr, 1, 2)

print("3D array after swapping axes:")
print(arr_swapped)