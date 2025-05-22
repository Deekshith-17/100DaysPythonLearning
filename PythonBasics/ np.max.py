import numpy as np

# Create a 2D array
data_2d = np.array([[1, 3, 5], [2, 4, 6], [7, 8, 9]])

# Calculate the maximum value along axis 0 (columns)
max_axis_0 = np.max(data_2d, axis=0)

# Calculate the maximum value along axis 1 (rows)
max_axis_1 = np.max(data_2d, axis=1)

print("Maximum value along axis 0:", max_axis_0)
print("Maximum value along axis 1:", max_axis_1)