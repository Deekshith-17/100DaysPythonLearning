import numpy as np

# Define a 2x2 matrix
A = np.array([[4, -2], 
              [1,  1]])

# Compute the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)