import numpy as np

# Creating an array
array = np.array([1, 5, 8, 12, 20, 3])

# Define the condition
condition = array > 10

# Apply the condition to filter the array
filtered_array = array[condition]

print("Original Array:", array)
print("Filtered Array (elements > 10):", filtered_array)