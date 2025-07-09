import pandas as pd
import numpy as np
s = pd.Series([1,2,3,4,5,4])
print(s.pct_change())

df = pd.DataFrame(np.random.randn(5, 2))
print(df.pct_change())