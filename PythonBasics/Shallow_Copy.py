import numpy as np

# Original array
original_array = np.array([[1, 2, 3], [4, 5, 6]])

# Shallow copy
shallow_copy = original_array.view()

# Modify an element in the shallow copy
shallow_copy[0, 0] = 100

print("Original Array:")
print(original_array)

print("\nShallow Copy:")
print(shallow_copy)    