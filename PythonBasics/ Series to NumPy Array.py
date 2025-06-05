import pandas as pd

# Create a Pandas Series
s = pd.Series([1, 2, 3])

# Convert Series to a NumPy Array
result = s.to_numpy()

print("Output:",result)
print("Output Type:", type(result))