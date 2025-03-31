import numpy as np

# Create a 2-dimensional NumPy array
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Get the dimensions of the array
rows, cols = arr_2d.shape

# Iterate over the array using indices
for i in range(rows):
   for j in range(cols):
      print(f"Element at ({i}, {j}): {arr_2d[i, j]}")