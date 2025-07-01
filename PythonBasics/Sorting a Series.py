import pandas as pd

panda_series = pd.Series([18, 95, 66, 12, 55, 0])
print("Unsorted Pandas Series: \n", panda_series)

panda_series_sorted = panda_series.sort_values(ascending=True)
print("\nSorted Pandas Series: \n", panda_series_sorted)