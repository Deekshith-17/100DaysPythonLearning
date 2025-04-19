import numpy as np

# Create three 1D arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array3 = np.array([7, 8, 9])

# Stack along the first axis (new axis 0)
stacked_array = np.stack((array1, array2, array3), axis=0)

print("Stacked Array:\n", stacked_array)
print("Shape of Stacked Array:", stacked_array.shape)