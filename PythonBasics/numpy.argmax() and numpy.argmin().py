import numpy as np 

# Create a 2D array
a = np.array([[30, 40, 70], [80, 20, 10], [50, 90, 60]])

print("Our array is:",a)

# Apply argmax() function
print("Applying argmax() function:",np.argmax(a))

# Index of maximum number in flattened array
print("Index of maximum number in flattened array:",a.flatten())

# Array containing indices of maximum along axis 0
print("Array containing indices of maximum along axis 0:")
maxindex = np.argmax(a, axis=0)
print(maxindex)


# Array containing indices of maximum along axis 1
print("Array containing indices of maximum along axis 1:")
maxindex = np.argmax(a, axis=1)
print(maxindex)

# Apply argmin() function
print("Applying argmin() function:")
minindex = np.argmin(a)
print(minindex)

# Flattened array
print("Flattened array:",a.flatten()[minindex])

# Flattened array along axis 0
print("Flattened array along axis 0:")
minindex = np.argmin(a, axis=0)
print(minindex)

# Flattened array along axis 1
print("Flattened array along axis 1:")
minindex = np.argmin(a, axis=1)
print(minindex)