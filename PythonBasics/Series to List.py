import pandas as pd

# Create a Pandas Series
s = pd.Series([1, 2, 3])

# Convert Series to a Python list
result = s.to_list()

print("Output:",result)
print("Output Type:", type(result))