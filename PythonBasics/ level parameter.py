import pandas as pd

# Create a MultiIndex object
index = pd.MultiIndex.from_tuples([('D', 'z'), ('D', 'x'), ('D', 'y'),('B', 't'), ('B', 's'), ('B', 'v')],
names=["level0", "level1"])

# Create a DataFrame
data = [[1, 2], [3, 4], [1, 1], [5, 6], [7, 8], [2, 2]]
df = pd.DataFrame(data, index=index, columns=['X', 'Y'])

# Display the input DataFrame
print('Original MultiIndexed DataFrame:\n',df)

# Sort by the level name
sorted_df = df.sort_index(level='level1')
print("Resultant DataFrame:")
print(sorted_df)