import numpy as np

# Create a structured array
structured_array = np.array([('Alice', 25, 5.5), ('Bob', 30, 6.0)], dtype=[('name', 'U10'), ('age', 'i4'), ('height', 'f4')])

# Convert the structured array to a record array
record_array = structured_array.view(np.recarray)

# Access fields as attributes
print(record_array.name)  
print(record_array.age)  