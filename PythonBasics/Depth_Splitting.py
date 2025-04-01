import numpy as np

# Example 3D array
arr = np.arange(24).reshape((2, 3, 4))

# Split into 4 equal parts along axis 2 (depth)
split_arr = np.dsplit(arr, 4)

print("Original Array:")
print(arr)
print("\nSplit into 4 equal parts along axis 2 (depth):")
for sub_arr in split_arr:
   print(sub_arr)
   print()