import numpy as np

# Step 1: Define the initial record array with fields 'name', 'age', and 'height'
dtype = [('name', 'S20'), ('age', 'i1'), ('height', 'f4')]
data = [('Alice', 30, 5.5), ('Bob', 25, 6.0), ('Charlie', 35, 5.8)]
record_array = np.array(data, dtype=dtype)

print("Original Record Array:")
print(record_array)

# Step 2: Update the fields for specific records
# Update 'age' and 'height' for 'Bob'
record_array[record_array['name'] == b'Bob']['age'] = 26
record_array[record_array['name'] == b'Bob']['height'] = 6.1

# Update 'age' for 'Charlie'
record_array[record_array['name'] == b'Charlie']['age'] = 36

print("\nUpdated Record Array:")
print(record_array)