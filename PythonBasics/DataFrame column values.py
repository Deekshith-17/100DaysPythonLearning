import pandas as pd

# Create a DataFrame
df= pd.DataFrame({'A': [1, 2, 3],'B': ['a', 'b', 'f']})

# Dispaly the Input DataFrame
print('Original DataFrame:\n', df)

# Define a mask for specific values in column 'A' and 'B'
mask = df['A'].isin([1, 3]) | df['B'].isin(['a'])

# Apply the mask using the boolean indexing
filtered_data = df[mask]

print('Filtered Data:\n', filtered_data)