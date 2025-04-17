import numpy as np

# Creating an array
array = np.array([1, 5, 8, 12, 20, 3])

# Define the condition
condition = array > 10

# Filter elements
filtered_indices = np.where(condition)
filtered_array = array[filtered_indices]

print("Original Array:", array)
print("Filtered Array (elements > 10) using np.where:", filtered_array)