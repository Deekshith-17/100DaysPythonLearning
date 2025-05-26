import pandas as pd

# Create MultiIndex
arrays = [[1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]
multi_idx = pd.MultiIndex.from_arrays(arrays, names=('number', 'color'))

# Create a DataFrame with MultiIndex
df = pd.DataFrame({'Col1': [1, 2, 3, 4], 'Col2':[1, 3, 5, 8]}, index=multi_idx)

print("MultiIndexed DataFrame:\n",df)