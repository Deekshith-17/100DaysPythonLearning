import numpy as np

# Create a record array
record_array = np.rec.array([('Alice', 25, 5.5), ('Bob', 30, 6.0)], dtype=[('name', 'U10'), ('age', 'i4'), ('height', 'f4')])

# Access multiple fields using indexing
multiple_fields = record_array[['name', 'height']]
print(multiple_fields)