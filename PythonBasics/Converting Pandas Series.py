import pandas as pd

# Create a Pandas Series
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

# Convert Series to a Python dictionary
result = s.to_dict()

print("Output:",result)
print("Output Type:", type(result))