import numpy as np

# Step 1: Define the initial record array with fields 'name' and 'age'
dtype = [('name', 'S20'), ('age', 'i1')]
data = [('Alice', 30), ('Bob', 25), ('Charlie', 35)]
record_array = np.array(data, dtype=dtype)

print("Original Record Array:")
print(record_array)

# Step 2: Define a new dtype that includes the new field 'height'
new_dtype = [('name', 'S20'), ('age', 'i1'), ('height', 'f4')]

# Step 3: Create a new record array with the new dtype, initialized with zeros or default values
new_record_array = np.zeros(record_array.shape, dtype=new_dtype)

# Step 4: Copy existing data into the new record array
for field in ['name', 'age']:
    new_record_array[field] = record_array[field]

# Optionally, set default values for the new field 'height'
new_record_array['height'] = 0.0

print("\nRecord Array with New Field:")
print(new_record_array)