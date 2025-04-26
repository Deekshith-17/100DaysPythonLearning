import numpy as np

# Define an array with duplicate rows
array = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3],
    [7, 8, 9]
])

# Find unique rows and their counts
unique_rows, counts = np.unique(array, axis=0, return_counts=True)

print("Unique Rows:\n", unique_rows)
print("Counts of Each Row:\n", counts)