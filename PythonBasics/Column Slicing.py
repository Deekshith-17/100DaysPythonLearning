import pandas as pd

data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# Slice a single column
col_A = df.iloc[:, 0]
print("Slicing a single column A using iloc[]:")
print(col_A)

# Slice multiple columns
cols_AB = df.iloc[:, 0:2]
print("Slicing multiple columns A and B using iloc[]:")
print(cols_AB)