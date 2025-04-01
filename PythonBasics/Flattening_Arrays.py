import numpy as np

# array
arr = np.array([[1, 2],
                [3, 4]])

# Flatten array
flattened_arr = arr.flatten()

# Find maximum value
max_value = np.max(flattened_arr)

print("Original Array:")
print(arr)
print("\nFlattened Array:")
print(flattened_arr)
print("\nMaximum Value in Flattened Array:",max_value)