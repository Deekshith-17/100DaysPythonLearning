import numpy as np

# Creating two arrays for comparison
array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([15, 20, 25, 40, 55])

# Performing element-wise comparisons
equality = array1 == array2
inequality = array1 != array2
greater_than = array1 > array2
less_than = array1 < array2
greater_equal = array1 >= array2
less_equal = array1 <= array2

# Displaying the results
print("Equality:", equality)
print("Inequality:", inequality)
print("Greater than:", greater_than)
print("Less than:", less_than)
print("Greater than or equal to:", greater_equal)
print("Less than or equal to:", less_equal)