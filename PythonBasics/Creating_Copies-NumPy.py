import numpy as np

# Original array
original_array = np.array([1, 2, 3])

# Creating a copy
copied_array = original_array.copy()

# Modifying the copy
copied_array[0] = 10

print("Original Array:", original_array)  
print("Copied Array:", copied_array)     