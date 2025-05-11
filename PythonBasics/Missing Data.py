import numpy as np

# Creating an array with missing values
arr = np.array([1, 2, np.nan, 4, np.nan, 6])

# Checking for missing values
is_nan = np.isnan(arr)

print("Array with Missing Values:\n", arr)
print("Missing Value Mask:\n", is_nan)