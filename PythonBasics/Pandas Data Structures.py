import pandas as pd

data = ['Steve', '35', 'Male', '3.5']
series = pd.Series(data, index=['Name', 'Age', 'Gender', 'Rating'])
print(series)