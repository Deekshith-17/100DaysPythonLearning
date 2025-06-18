import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3, 4, 5],'B': [4, 5, 6, 7, 8],
'C': [9, 10, 11, 12, 13]}, index=['r1', 'r2', 'r3', 'r4', 'r5'])

# Display original DataFrame
print("Original DataFrame:")
print(df)

# Drop the rows by row-labels
result = df.drop(['r1', 'r3'])

# Display the result
print("\nAfter dropping the rows:")
print(result)