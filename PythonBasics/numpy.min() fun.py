import numpy as np

# Create a 3D array
data_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Minimum value along axis 0
min_3d_axis_0 = np.min(data_3d, axis=0)

# Minimum value along axis 1
min_3d_axis_1 = np.min(data_3d, axis=1)

# Minimum value along axis 2
min_3d_axis_2 = np.min(data_3d, axis=2)

print("Minimum value along axis 0:", min_3d_axis_0)
print("Minimum value along axis 1:", min_3d_axis_1)
print("Minimum value along axis 2:", min_3d_axis_2)