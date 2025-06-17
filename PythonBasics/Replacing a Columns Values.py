import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3],'B': [4, 5, 6]})

# Replace the contents of column 'A' with new values
df['A'] = [10, 20, 30]

# Display updated DataFrame
print("DataFrame after replacing column 'A':")
print(df)