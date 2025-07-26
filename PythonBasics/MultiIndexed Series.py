import pandas as pd
import numpy as np

# Create a 2D list
list_2d = [["BMW", "BMW", "Lexus", "Lexus", "foo", "foo", "Audi", "Audi"],
["1", "2", "1", "2", "1", "2", "1", "2"]]

# Create a MultiIndex object
index = pd.MultiIndex.from_arrays(list_2d, names=["first", "second"])

# Creating a MultiIndexed Series
s = pd.Series(np.random.randn(8), index=index)

# Display the output Series 
print("Output MultiIndexed Series:\n",s)