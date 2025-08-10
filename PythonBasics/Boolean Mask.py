import pandas as pd

# Create a Pandas Series
s = pd.Series([1, 5, 2, 8, 4], index=['A', 'B', 'C', 'D', 'E'])

# Display the Series
print("Input Series:")
print(s)

# Create Boolean mask
result = s > 2

print('\nBoolean Mask:')
print(result)