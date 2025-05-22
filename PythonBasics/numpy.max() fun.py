import numpy as np

# Create a 3D array
data_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Maximum value along axis 0
max_3d_axis_0 = np.max(data_3d, axis=0)

# Maximum value along axis 1
max_3d_axis_1 = np.max(data_3d, axis=1)

# Maximum value along axis 2
max_3d_axis_2 = np.max(data_3d, axis=2)

print("Maximum value along axis 0:", max_3d_axis_0)
print("Maximum value along axis 1:", max_3d_axis_1)
print("Maximum value along axis 2:", max_3d_axis_2)