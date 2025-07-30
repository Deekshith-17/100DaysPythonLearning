import pandas as pd

# Create a MultiIndex object
index = pd.MultiIndex.from_tuples([('A', 'one'), ('A', 'two'), ('A', 'three'),('B', 'one'), ('B', 'two'), ('B', 'three')])
# Create a DataFrame
data = [[1, 2], [3, 4], [1, 1], [5, 6], [7, 8], [2, 2]]
df = pd.DataFrame(data, index=index, columns=['X', 'Y'])

# Display the input DataFrame
print('Original MultiIndexed DataFrame:\n',df)

# New index for reindexing
new_index = [('A', 'one'), ('foo', 'two'), ('B', 'two'), ('A', 'three'), ('B', 'one'), ('A', 'two')]

# Reindexing the DataFrame
reindexed_df = df.reindex(new_index)

print('\nReindexed DataFrame:\n', reindexed_df)