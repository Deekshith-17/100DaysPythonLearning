import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': [1, 3, 5, 7],'B': [5, 2, 8, 4],'C': ['x', 'y', 'x', 'z']})

# Display the DataFrame
print("Input DataFrame:\n", df)

# Apply multiple conditions using boolean indexing
result = df.loc[(df['A'] > 2) & (df['B'] < 5), 'A':'C']

print('Output Filtered DataFrame:\n',result)