import numpy as np

# Creating an array
array = np.array([5, 10, 15, 20, 25, 30])

# Chaining multiple comparisons
result = (array > 10) & (array < 25) & (array % 5 == 0)

# Displaying the results
print("Array:", array)
print("Result of Chained Comparisons:", result)  