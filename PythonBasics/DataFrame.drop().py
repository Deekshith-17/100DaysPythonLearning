import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3],'B': [4, 5, 6],'C': [7, 8, 9]})

# Display the original DataFrame
print("Original DataFrame:", df, sep='\n')

# Delete columns 'A' and 'B'
df = df.drop(columns=['A', 'B'])

# Display updated DataFrame
print("DataFrame after deleting columns 'A' and 'B':")
print(df)