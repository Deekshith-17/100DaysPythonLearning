import pandas as pd

# Creating a CategoricalIndex
categories = pd.CategoricalIndex(['a','b', 'a', 'c'])
df = pd.DataFrame({'Col1': [50, 70, 90, 60], 'Col2':[1, 3, 5, 8]}, index=categories)
print("Input DataFrame:\n",df)

print("\nDataFrame Index Object Type:",df.index.dtype)