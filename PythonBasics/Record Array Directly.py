import numpy as np 

# Directly create a record array
record_array_direct = np.rec.array([('Charlie', 35, 5.8), ('David', 40, 6.2)], dtype=[('name', 'U10'), ('age', 'i4'), ('height', 'f4')])

# Access fields as attributes
print(record_array_direct.name)   
print(record_array_direct.height) 