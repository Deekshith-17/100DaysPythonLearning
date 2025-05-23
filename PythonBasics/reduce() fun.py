import numpy as np
from functools import reduce

# Define multiple arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([3, 4, 5, 6, 7])
array3 = np.array([5, 6, 7, 8])

# Calculate the difference of all arrays
difference = reduce(lambda x, y: np.setdiff1d(x, y), [array1, array2, array3])

print("Difference of multiple arrays:", difference)