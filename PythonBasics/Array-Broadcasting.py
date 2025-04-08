import numpy as np

# Creating arrays with different shapes
a = np.array([[10, 20, 30], [40, 50, 60]])
b = np.array([10, 5, 2])

# Performing division with broadcasting
result = a / b
print(result)