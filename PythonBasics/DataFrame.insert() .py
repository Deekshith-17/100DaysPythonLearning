import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3],'B': [4, 5, 6]})

# Insert a new column 'D' at position 1
df.insert(1, 'D', [10, 11, 12])

# Display updated DataFrame
print("DataFrame after inserting column 'D' at position 1:")
print(df)