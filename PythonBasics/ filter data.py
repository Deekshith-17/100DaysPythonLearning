import pandas as pd

# Create a sample DataFrame
df= pd.DataFrame({'Col1': [1, 3, 5, 7, 9],
'Col2': ['A', 'B', 'A', 'C', 'A']})

# Display the Input DataFrame
print('Original DataFrame:\n', df)

# Create a boolean mask
mask = (df['Col2'] == 'A') & (df['Col1'] > 4)

# Apply the mask to the DataFrame
filtered_data = df[mask]

print('Filtered Data:\n',filtered_data)