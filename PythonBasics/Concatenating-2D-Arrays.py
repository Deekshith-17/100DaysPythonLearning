import numpy as np

# Create two 2D arrays
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

# Concatenate along axis 0 (row-wise)
result_axis_0 = np.concatenate((array1, array2), axis=0)

print("Concatenated along Axis 0:\n", result_axis_0)

# Concatenate along axis 1 (column-wise)
result_axis_1 = np.concatenate((array1, array2), axis=1)

print("Concatenated along Axis 1:\n", result_axis_1)