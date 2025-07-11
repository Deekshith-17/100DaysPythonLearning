import pandas as pd
import numpy as np

def adder(ele1,ele2):
   return ele1+ele2

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
print('Original DataFrame:\n', df)

df.pipe(adder,2)
print('Modified DataFrame:\n', df)