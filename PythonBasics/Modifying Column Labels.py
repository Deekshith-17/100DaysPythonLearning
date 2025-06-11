import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'Name': ['Steve', 'Lia', 'Vin', 'Katie'],
    'Age': [32, 28, 45, 38],
    'Gender': ['Male', 'Female', 'Male', 'Female'],
    'Rating': [3.45, 4.6, 3.9, 2.78]},
    index=['r1', 'r2', 'r3', 'r4'])
    
# Display the Input DataFrame
print('Input DataFrame:\n', df)

# Modify the Column labels of the DataFrame
df.columns = ['Col1', 'Col2', 'Col3', 'Col4']
print('Output Modified DataFrame with the updated Column Labels\n:', df)