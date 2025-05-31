import pandas as pd
import numpy as np

data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data)

# Display the Original series
print('Original Series:',s, sep='\n')

# Slice the range of values
result = s[1:3]

# Display the output
print('Values after slicing the Series:', result, sep='\n')