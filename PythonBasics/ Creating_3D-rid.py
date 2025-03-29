import numpy as np

# Create 1D arrays for x, y, and z coordinates
x = np.arange(1, 4)
y = np.arange(1, 3)
z = np.arange(1, 3)

# Generate coordinate matrices
X, Y, Z = np.meshgrid(x, y, z, indexing='ij')

print("X grid:")
print(X)
print("Y grid:")
print(Y)
print("Z grid:")
print(Z)