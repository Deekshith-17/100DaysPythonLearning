import pandas as pd
import numpy as np

# Create MultiIndex
tuples = [["x", "x", "y", "y", "", "f", "z", "z"],["1", "2", "1", "2", "1", "2", "1", "2"]]
index = pd.MultiIndex.from_arrays(tuples, names=["first", "second"])

# Create a DataFrame
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])

# Display the input DataFrame
print('Input DataFrame:\n', df)

# Stack columns
stacked = df.stack()

print('Output Reshaped DataFrame:\n', stacked)