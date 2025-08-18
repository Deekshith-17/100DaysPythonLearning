import pandas as pd

# Create a DataFrame
index = pd.MultiIndex.from_tuples([("person", "A"), ("person", "B")])
df= pd.DataFrame({
"first": ["John", "Mary"],"last": ["Doe", "Bo"],
"height": [5.5, 6.0],"weight": [130, 150]}, index=index)

# Display the input DataFrame
print('Input DataFrame:\n', df)

# Melt the DataFrame
melted_df = pd.melt(df, id_vars=["first", "last"], ignore_index=False)

print('Output melted DataFrame:\n', melted_df)