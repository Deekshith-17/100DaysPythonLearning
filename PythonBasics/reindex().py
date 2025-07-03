import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
print("Original Series:\n",s)

s_reindexed = s.reindex(["e", "b", "f", "d"])
print('\nOutput Reindexed Series:\n',s_reindexed)