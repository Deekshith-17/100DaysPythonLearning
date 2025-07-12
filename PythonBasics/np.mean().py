import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), columns=['col1', 'col2', 'col3'])
print('Original DataFrame:\n', df)

result = df.apply(np.mean, axis=1)
print('Result:\n',result)