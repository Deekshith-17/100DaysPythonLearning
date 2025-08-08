import pandas as pd

# Create a Pandas DataFrame
df = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['A', 'B'])

# Display the DataFrame
print("Input DataFrame:\n", df)

# Create Boolean Index
s = (df['A'] > 2)

# Filter data using .iloc and the Boolean Index
print('Output Filtered Data:\n',df.iloc[s.values, 1])