import numpy as np
# Creating an array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Chaining comparisons with scalar values
result = (array >= 3) & (array <= 7)

# Displaying the results
print("Array:", array)
print("Result of Chained Comparisons with Scalar:", result)   