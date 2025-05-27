import pandas as pd

# Create PeriodIndex
period_idx = pd.PeriodIndex(year=[2020, 2024], quarter=[1, 3])

# Create a DataFrame with PeriodIndex
df = pd.DataFrame({'Col1': [1, 2], 'Col2':[1, 3]}, index=period_idx )

print("PeriodIndexed DataFrame:\n",df)