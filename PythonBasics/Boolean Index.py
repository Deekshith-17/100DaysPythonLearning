import pandas as pd

# Create a Pandas DataFrame
df = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['A', 'B'])

# Display the DataFrame
print("Input DataFrame:\n", df)

# Create Boolean Index
result = df > 2

print('Boolean Index:\n', result)