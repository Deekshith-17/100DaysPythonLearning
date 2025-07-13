import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), columns=['col1', 'col2', 'col3'])
print('Original DataFrame:\n', df)

result = df.apply(lambda x: x.max() - x.min())
print('Result:\n',result)