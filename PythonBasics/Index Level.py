import pandas as pd
import numpy as np

# Creating MultiIndex from arrays
arrays = [["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
["one", "two", "one", "two", "one", "two", "one", "two"]]

# Creating a list of tuples from the arrays
tuples = list(zip(*arrays))

# Creating a MultiIndex from tuples
index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])

# Creating a Series with MultiIndex
s = pd.Series([2, 3, 1, 4, 6, 1, 7, 8], index=index)

print("MultiIndexed Series:\n", s)

# Indexing the MultiIndexed Series using .loc[]
print("\nSelecting data at index ('bar', 'one') and column 'A':")
print(s.loc[('bar', 'one')])