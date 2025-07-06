import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])

print("Original DataFrame:\n", df)

# Iterate Through DataFrame rows
print("Iterated Output:")
for row in df.itertuples():
   print(row)