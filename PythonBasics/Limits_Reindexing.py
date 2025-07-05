import pandas as pd
import numpy as np
 
df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])

# Padding NaNs
print(df2.reindex_like(df1))

# Now fill the NaNs with preceding values
print("Data Frame with Forward Fill limiting to 1:")
print(df2.reindex_like(df1, method='ffill', limit=1))