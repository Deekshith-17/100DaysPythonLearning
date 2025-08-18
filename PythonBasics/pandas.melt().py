import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},'B': {0: 1, 1: 3, 2: 5},'C': {0: 2, 1: 4, 2: 6}})

# Display the input DataFrame
print('Input DataFrame:\n', df)

# Melt the DataFrame
melted_df = pd.melt(df, id_vars=['A'], value_vars=['B'])

print('Output melted DataFrame:\n', melted_df)