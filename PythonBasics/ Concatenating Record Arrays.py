import numpy as np

# Define two record arrays with fields 'name', 'age', and 'height'
dtype = [('name', 'U10'), ('age', 'i4'), ('height', 'f4')]
data1 = [('Alice', 25, 5.5), ('Bob', 30, 6.0)]
data2 = [('Charlie', 35, 5.8), ('David', 40, 5.9)]

# Create record arrays
record_array1 = np.array(data1, dtype=dtype).view(np.recarray)
record_array2 = np.array(data2, dtype=dtype).view(np.recarray)

# Concatenate the record arrays along the rows (axis 0)
combined_record_array = np.concatenate((record_array1, record_array2))

print("Combined record array:")
print(combined_record_array)