import pandas as pd
import numpy as np

# Create a DataFrame
df = pd.DataFrame({"keys": list("aeeioou"), "values": range(7)})

# Display the Input DataFrame
print('Input DataFrame:\n',df)

# Create dummy variables for the keys column
dummies = pd.get_dummies(df["keys"])
print('Resultant Dummy Variables:\n',dummies)