import pandas as pd

# Create a DataFrame with labeled indices
df = pd.DataFrame([['a','b'], ['c','d'], ['e','f'], ['g','h']], columns=['col1', 'col2'], index=['r1', 'r2', 'r3', 'r4'])

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Slice rows and columns by label
result = df.loc['r1':'r3', 'col1']
print("Output:")
print(result)