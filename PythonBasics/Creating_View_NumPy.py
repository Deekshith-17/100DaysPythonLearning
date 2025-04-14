import numpy as np

# Original array
original_array = np.array([1, 2, 3])

view_array = original_array[0:2]

# Modifying the view
view_array[0] = 30

print("Original Array after view modification:", original_array) 
print("View Array:", view_array)                                   