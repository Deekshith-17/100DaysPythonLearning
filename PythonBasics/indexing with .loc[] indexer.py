import pandas as pd

# Create a MultiIndex object
index = pd.MultiIndex.from_tuples([('A', 'one'), ('A', 'two'), ('B', 'one'), ('B', 'two')])

# Create a DataFrame
data = [[1, 2], [3, 4], [5, 6], [7, 8]]
df = pd.DataFrame(data, index=index, columns=['X', 'Y'])

# Display the input DataFrame
print('Original MultiIndexed DataFrame:\n',df)

# Select specific element 
print('Selected data:')
print(df.loc[('A', 'two'), 'Y']) 