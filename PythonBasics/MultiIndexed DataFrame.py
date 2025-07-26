import pandas as pd
import numpy as np

# Create a 2D list
list_2d = [["BMW", "BMW", "Lexus", "Lexus", "foo", "foo", "Audi", "Audi"],
["1", "2", "1", "2", "1", "2", "1", "2"]]

# Create a MultiIndex object
tuples = list(zip(*list_2d ))
index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])

# Creating a MultiIndexed DataFrame
df = pd.DataFrame(np.random.randn(8, 4), index=index, columns=["A", "B", "C", "D"])

# Display the output Series 
print("Output MultiIndexed DataFrame:\n", df)