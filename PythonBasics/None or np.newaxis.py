import numpy as np

# Creating a 1D NumPy array
arr = np.array([1, 2, 3, 4])

# Adding a new axis to create a 2D row vector
row_vector = arr[:, np.newaxis]

print("Original Array:\n", arr)
print("2D Row Vector:\n", row_vector)