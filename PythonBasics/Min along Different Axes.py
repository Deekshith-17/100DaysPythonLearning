import numpy as np

# Create a 2D array
data_2d = np.array([[1, 3, 5], [2, 4, 6], [7, 8, 9]])

# Calculate the minimum value along axis 0 (columns)
min_axis_0 = np.min(data_2d, axis=0)

# Calculate the minimum value along axis 1 (rows)
min_axis_1 = np.min(data_2d, axis=1)

print("Minimum value along axis 0:", min_axis_0)
print("Minimum value along axis 1:", min_axis_1)