import numpy as np

# Create two 2D arrays
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
 
# Stack along a new third axis (axis 2)
stacked_array = np.stack((array1, array2), axis=2)

print("Stacked Array along Axis 2:\n", stacked_array)
print("Shape of Stacked Array:", stacked_array.shape)