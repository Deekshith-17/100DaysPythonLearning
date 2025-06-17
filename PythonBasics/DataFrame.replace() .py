import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3],'B': [4, 5, 6]})

# Display the Input DataFrame 
print("Original DataFrame:", df, sep='\n')

# Replace the contents 
df.replace({'A': 1, 'B': 6}, 100, inplace=True)

# Display updated DataFrame
print("DataFrame after replacing column 'A':")
print(df)