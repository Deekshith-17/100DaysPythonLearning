import numpy as np

# Vertically stack two arrays
array1 = np.array([[1, 2, 3],
                   [4, 5, 6]])
array2 = np.array([[7, 8, 9],
                   [10, 11, 12]])

vstacked_array = np.vstack((array1, array2))

# Split the array back into the original arrays
split_arrays = np.vsplit(vstacked_array, 2)

print("Split Arrays:")
for arr in split_arrays:
   print(arr)