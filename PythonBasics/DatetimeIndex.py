import pandas as pd

# Create DatetimeIndex
datetime_idx = pd.DatetimeIndex(["2020-01-01 10:00:00", "2020-02-01 11:00:00"])

# Create a DataFrame with DatetimeIndex
df = pd.DataFrame({'Col1': [1, 2], 'Col2':[1, 3]}, index=datetime_idx )

print("DatetimeIndexed DataFrame:\n",df)