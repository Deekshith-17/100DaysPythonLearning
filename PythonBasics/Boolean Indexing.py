import pandas as pd

# Create a MultiIndex object
index = pd.MultiIndex.from_tuples([('A', 'one'), ('A', 'two'), ('B', 'one'), ('B', 'two')])

# Create a DataFrame
data = [[1, 2], [3, 4], [5, 6], [7, 8]]
df = pd.DataFrame(data, index=index, columns=['X', 'Y'])

# Display the input DataFrame
print('Original MultiIndexed DataFrame:\n',df)

# Select data based on the boolean indexing
print('Selected data:')   
mask = df['X'] > 2
print(df[mask])  