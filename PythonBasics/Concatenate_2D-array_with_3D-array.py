import numpy as np

# Create a 2D array
arr1 = np.array([[1, 2],
                 [3, 4]])

# Create a 3D array
arr2 = np.array([[[5, 6],
                  [7, 8]],
                 
                 [[9, 10],
                  [11, 12]]])

# Expand dimensions of the 2D array to match the 3D array for concatenation along the third dimension (axis=2)
expanded_arr1 = np.expand_dims(arr1, axis=2)

# Concatenate along the third dimension (axis=2)
concatenated_arr = np.concatenate((expanded_arr1, arr2), axis=2)
print("Concatenated Array with Mixed Dimensions along axis=2:")
print(concatenated_arr)