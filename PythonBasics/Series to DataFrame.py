import pandas as pd

# Create a Pandas Series
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

# Convert Series to a Pandas DataFrame
result = s.to_frame(name='Numbers')

print("Output:\n",result)
print("Output Type:", type(result))