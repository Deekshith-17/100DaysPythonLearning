import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3],'B': [4, 5, 6]}, index=['x', 'y', 'z'])

# Display original DataFrame
print("Original DataFrame:")
print(df)

# Rename the multiple row labels
df = df.rename(index={'x': 'r1', 'y':'r2', 'z':'r3'})

# Display modified DataFrame
print("Modified DataFrame:")
print(df)