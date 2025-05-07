import numpy as np

# Creating a 3D NumPy array
arr = np.array([[[1, 2, 3], [4, 5, 6]], 
                [[7, 8, 9], [10, 11, 12]]])

# Swapping the first and last columns along the second axis
arr[:, :, [0, 2]] = arr[:, :, [2, 0]]

print("3D array after swapping columns:")
print(arr)