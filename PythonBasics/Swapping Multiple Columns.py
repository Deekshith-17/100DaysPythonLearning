import numpy as np

# Create a 2D array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Swap columns in the order: 1st to 3rd, 2nd to 1st, 3rd to 2nd
arr[:, [0, 1, 2]] = arr[:, [1, 2, 0]]

print("Array after swapping columns:")
print(arr)