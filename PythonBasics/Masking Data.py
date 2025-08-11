import pandas as pd

# Create a DataFrame with a custom index
df = pd.DataFrame({'A1': [10, 20, 30, 40, 50], 'A2':[9, 3, 5, 3, 2]
}, index=['a', 'b', 'c', 'd', 'e'])

# Dispaly the Input DataFrame
print('Original DataFrame:\n', df)

# Define a mask based on the index
mask = df.index.isin(['b', 'd'])

# Apply the mask
filtered_data = df[mask]

print('Filtered Data:\n',filtered_data)