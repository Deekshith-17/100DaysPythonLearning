import pandas as pd

# Create a DataFrame
df = pd.DataFrame([['a', 'b'], ['c', 'd'], ['e', 'f'], ['g', 'h']], 
                  columns=['col1', 'col2'])

# Display the Original DataFrame
print("Original DataFrame:", df, sep='\n')

# Modify a subset of the DataFrame using iloc
df.iloc[1:3, 0] = ['x', 'y']

# Display the modified DataFrame
print('Modified DataFrame:',df, sep='\n')