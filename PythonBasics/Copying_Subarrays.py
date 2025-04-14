import numpy as np

# Original 2D array
original_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Creating a copy of the subarray
sub_array = original_array[0:2].copy()
sub_array[0] = 20

print("Original Array after subarray copy:", original_array)  
print("Subarray:", sub_array)                                 