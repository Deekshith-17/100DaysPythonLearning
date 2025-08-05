import pandas as pd

# Create arrays
arrays = [[2, 4, 3, 1], ['Peter', 'Chris', 'Andy', 'Jacob']]

# The from_arrays() is used to create a MultiIndex
multiIndex = pd.MultiIndex.from_arrays(arrays, names=('ranks', 'student'))

# display the MultiIndex
print("The Multi-index...\n",multiIndex)

# Sort MultiIndex using the sort_values() method
print("\nSort MultiIndex...\n",multiIndex.sort_values())