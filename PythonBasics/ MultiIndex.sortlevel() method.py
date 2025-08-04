import pandas as pd

# Create arrays
arrays = [[2, 4, 3, 1], ['Peter', 'Chris', 'Andy', 'Jacob']]

# The from_arrays() is used to create a MultiIndex
multiIndex = pd.MultiIndex.from_arrays(arrays, names=('ranks', 'student'))

# display the MultiIndex
print("The Multi-index...\n",multiIndex)

# get the levels in MultiIndex
print("\nThe levels in Multi-index...\n",multiIndex.levels)

# Sort MultiIndex
# The specific level to sort is set as a parameter i.e. level 1 here
print("\nSort MultiIndex at the requested level...\n",multiIndex.sortlevel(1))