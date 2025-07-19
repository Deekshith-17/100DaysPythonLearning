import pandas as pd

# Creating a series
s = pd.Series(range(10))

# Applying a triangular weighted window
result = s.rolling(window=5, win_type="triang").mean()
print(result)