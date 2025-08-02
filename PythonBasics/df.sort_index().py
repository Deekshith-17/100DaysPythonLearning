import pandas as pd

# Create a MultiIndex object
index = pd.MultiIndex.from_tuples([('A', 'one'), ('A', 'two'), ('A', 'three'),('B', 'one'), ('B', 'two'), ('B', 'three')],
names=["level0", "level1"])

# Create a DataFrame
data = [[1, 2], [3, 4], [1, 1], [5, 6], [7, 8], [2, 2]]
df = pd.DataFrame(data, index=index, columns=['X', 'Y'])

# Display the input DataFrame
print('Original MultiIndexed DataFrame:\n',df)

# Sort MultiIndex with default levels
sorted_df = df.sort_index()
print("Resultant DataFrame:")
print(sorted_df)