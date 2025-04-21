import numpy as np 

# Create an array
x = np.array([3, 1, 2])

print("Our array is:",x)

# Get indices that would sort the array
y = np.argsort(x)

print("Applying argsort() to x:",y)

# Reconstruct the sorted array using the indices
print("Reconstruct original array in sorted order:",x[y])

# Reconstruct the original array using a loop
print("Reconstruct the original array using loop:")
for i in y:
   print(x[i], end=' ')