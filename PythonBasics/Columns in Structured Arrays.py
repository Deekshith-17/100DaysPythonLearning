import numpy as np

# Create a structured array
dtype = [('A', 'i4'), ('B', 'i4'), ('C', 'i4')]
arr = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)], dtype=dtype)

# Swap columns 'A' and 'C'
arr[['A', 'C']] = arr[['C', 'A']]

print("Structured array after swapping columns 'A' and 'C':")
print(arr)