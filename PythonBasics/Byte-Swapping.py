import numpy as np

# Creating a NumPy array with 32-bit integers
arr = np.array([1, 256, 65535], dtype=np.int32)

print("Original Array:")
print(arr)

# Perform in-place byte swapping
arr.byteswap()

print("\nArray After In-Place Byte Swapping:")
print(arr)