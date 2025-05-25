import pandas as pd

# Creating a IntervalIndex
interval_idx = pd.interval_range(start=0, end=4)

# Creating a DataFrame with IntervalIndex
df = pd.DataFrame({'Col1': [1, 2, 3, 4], 'Col2':[1, 3, 5, 8]}, index=interval_idx)

print("Input DataFrame:\n",df)

print("\nDataFrame Index Object Type:",df.index.dtype)