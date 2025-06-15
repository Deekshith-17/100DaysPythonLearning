import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3],'B': [4, 5, 6]})

# Display original DataFrame
print("Original DataFrame:")
print(df)

# Rename column 'A' to 'aa'
df = df.rename(columns={'A': 'aa'})

# Display modified DataFrame
print("Modified DataFrame:")
print(df)