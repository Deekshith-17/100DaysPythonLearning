import numpy as np

# array
arr = np.arange(9).reshape(3, 3)

# Split into 3 equal sub-arrays 
split_arr = np.split(arr, 3, axis=1)

print("Original Array:")
print(arr)
print("\nSplit into 3 equal sub-arrays along axis 1:")
for sub_arr in split_arr:
   print(sub_arr)