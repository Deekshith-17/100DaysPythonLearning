import pandas as pd

# Create a Pandas Series
s = pd.Series([1, 2, 3], index=['r1', 'r2', 'r3'])

# Convert Series to string representation
result = s.to_string()

print("Output:",repr(result))
print("Output Type:", type(result))