import pandas as pd
import numpy as np

# Create a list of lits 
iterable = [[1, 2, 3], ['green', 'black']]

# Create a MultiIndex object
index = pd.MultiIndex.from_product(iterable, names=["number", "color"])

# Creating a MultiIndexed DataFrame
df = pd.DataFrame(np.random.randn(6, 3), index=index, columns=["A", "B", "C"])

# Display the output Series 
print("Output MultiIndexed DataFrame:\n", df)