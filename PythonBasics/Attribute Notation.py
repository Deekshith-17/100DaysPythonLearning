import numpy as np

# Create a record array
record_array = np.rec.array([('Alice', 25, 5.5), ('Bob', 30, 6.0)], dtype=[('name', 'U10'), ('age', 'i4'), ('height', 'f4')])

# Accessing the 'name' field
print(record_array.name)  

# Accessing the 'age' field
print(record_array.age)   

# Accessing the 'height' field
print(record_array.height) 