import pandas as pd
import numpy as np

# Create Data
index = pd.MultiIndex.from_product([["bar", "baz", "foo", "qux"], ["one", "two"]], names=["first", "second"])
columns = pd.MultiIndex.from_tuples([("A", "cat"), ("B", "dog"), ("B", "cat"), ("A", "dog")], names=["exp", "animal"])

df = pd.DataFrame(np.random.randn(8, 4), index=index, columns=columns)

# Create a DataFrame
df3 = df.iloc[[0, 1, 4, 7], [1, 2]]

print(df3)

# Unstack the DataFame
unstacked = df3.unstack()

# Display the Unstacked DataFrame
print("Unstacked DataFrame without Filling:\n",unstacked)

unstacked_filled = df3.unstack(fill_value=1)
print("Unstacked DataFrame with Filling:\n",unstacked_filled)