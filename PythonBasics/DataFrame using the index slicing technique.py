import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3, 4, 5],'B': [4, 5, 6, 7, 8]})

# Display original DataFrame
print("Original DataFrame:")
print(df)

# Drop the row using the index slicing
result = df.drop(df.index[2:4])

# Display the result
print("\nAfter dropping the row at 2 and 3:")
print(result)