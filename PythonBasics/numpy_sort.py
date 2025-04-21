import numpy as np  

# Create a 2D array
a = np.array([[3, 7], [9, 1]])

print("Our array is:",a)

# Default sort
print("Applying sort() function:",np.sort(a))

# Sort along axis 0
print("Sort along axis 0:",np.sort(a, axis=0))

# Order parameter in sort function
dt = np.dtype([('name', 'S10'), ('age', int)])
a = np.array([("raju", 21), ("anil", 25), ("ravi", 17), ("amar", 27)], dtype=dt)

print("Our array is:",a)

print("Order by name:",np.sort(a, order='name'))