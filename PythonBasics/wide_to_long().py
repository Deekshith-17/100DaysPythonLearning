import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'famid': [1, 1, 1, 2, 2, 2, 3, 3, 3],
'birth': [1, 2, 3, 1, 2, 3, 1, 2, 3],
'ht1': [2.8, 2.9, 2.2, 2, 1.8, 1.9, 2.2, 2.3, 2.1],
'ht2': [3.4, 3.8, 2.9, 3.2, 2.8, 2.4, 3.3, 3.4, 2.9]})

# Display the input DataFrame
print('Input DataFrame:\n', df)

# Melt the DataFrame using wide_to_long()
long_df = pd.wide_to_long(df, stubnames='ht', i=['famid', 'birth'], j='age')

print('Output Long Melted DataFrame:\n', long_df)