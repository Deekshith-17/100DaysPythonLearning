import numpy as np

# Create an array with some NaN values
arr = np.array([1.0, 2.0, np.nan, 4.0, np.nan])

# Generate a boolean array indicating NaN values
nan_mask = np.isnan(arr)

# Filter out NaN values
filtered_arr = arr[~nan_mask]

print("Original array:")
print(arr)
print("Filtered array (without NaN values):")
print(filtered_arr)