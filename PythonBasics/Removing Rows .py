import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3, 4, 5],'B': [4, 5, 6, 7, 8],
'C': [90, 0, 11, 12, 13]}, index=['r1', 'r2', 'r3', 'r4', 'r5'])

# Display original DataFrame
print("Original DataFrame:")
print(df)

# Dropping rows where column 'C' contains 0
result = df[df["C"] != 0]

# Display the result
print("\nAfter dropping the row where 'C' has 0:")
print(result)