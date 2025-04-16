import numpy as np

# Creating an array
array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([15, 20, 25, 40, 55])

# Finding maximum and minimum values between two arrays
max_array = np.maximum(array1, array2)
min_array = np.minimum(array1, array2)

print("Maximum values:", max_array)
print("Minimum values:", min_array)