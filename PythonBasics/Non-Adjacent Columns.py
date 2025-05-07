import numpy as np

# Create a 2D array
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

# Swap the first (index 0) and third (index 2) columns
arr[:, [0, 2]] = arr[:, [2, 0]]

print("Array after swapping non-adjacent columns:")
print(arr)