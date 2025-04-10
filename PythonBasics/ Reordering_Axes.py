import numpy as np

# Creating a 3D array
arr = np.array([[[1, 2], [3, 4]],
                [[5, 6], [7, 8]]])

# Transposing with custom axis order
transposed = np.transpose(arr, (1, 0, 2))

print("Original Array Shape:", arr.shape)
print("Transposed Array Shape:", transposed.shape)
print("\nTransposed Array:")
print(transposed)