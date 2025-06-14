import pandas as pd

data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# Slice a single column by label
col_A = df.loc[:, 'A']
print("Slicing a single column A using loc[]:")
print(col_A)

# Slice multiple columns by label
cols_AB = df.loc[:, 'A':'B']
print("Slicing Multiple columns A and B using loc[]:")
print(cols_AB)