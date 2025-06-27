import pandas as pd
import numpy as np

# Generate a DataFrame with random integers
data = np.random.randint(0, 100, size=(1000, 5))
column_names = [f"Col_{i}" for i in range(1, 5 + 1)]

# Create a DataFrame and save it as a CSV file
large_csv_file = "large_file.csv"
df = pd.DataFrame(data, columns=column_names)
df.to_csv(large_csv_file, index=False)
print(f"Large CSV file is created successfully.\n")

# Read large CSV file in chunks
chunk_size = 200

print("Output CSV data in chunks:")
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
   print('Data in chunks:') 
   print(chunk.head(2))