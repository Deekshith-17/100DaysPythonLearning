import pandas as pd

# Create TimedeltaIndex
timedelta_idx = pd.TimedeltaIndex(['0 days', '1 days', '2 days'])

# Create a DataFrame with TimedeltaIndex
df = pd.DataFrame({'Col1': [1, 2, 3], 'Col2':[1, 3, 3]}, index=timedelta_idx )

print("TimedeltaIndexed DataFrame:\n",df)