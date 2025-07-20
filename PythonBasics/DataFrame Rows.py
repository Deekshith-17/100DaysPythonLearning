import pandas as pd
import numpy as np

df = pd.DataFrame([[1, 2, 3, 1],
                   [4, 5, 6, np.nan],
                   [7, 8, 9, 2],
                   [np.nan, 2, np.nan, 3]],
   index = pd.date_range('1/1/2024', periods=4),
   columns = ['A', 'B', 'C', 'D'])

print("Input DataFrame:\n",df)
result = df.agg(['sum', 'min'])
print("\nResults:\n",result)