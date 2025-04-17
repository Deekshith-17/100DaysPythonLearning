import numpy as np

# Creating an array
array = np.array([1, 5, 8, 12, 20, 3])

# Define multiple conditions
condition = (array > 5) & (array < 15)

# Apply the conditions to filter the array
filtered_array = array[condition]

print("Original Array:", array)
print("Filtered Array (5 < elements < 15):", filtered_array)  