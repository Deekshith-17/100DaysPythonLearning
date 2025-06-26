import pandas as pd

# Import StringIO to load a file-like object for reading CSV
from io import StringIO

# Create string representing CSV data
data = """Name,Gender,Age
Braund,male,22
Cumings,female,38
Heikkinen,female,26
Futrelle,female,35"""

# Use StringIO to convert the string data into a file-like object
obj = StringIO(data)

# read CSV into a Pandas DataFrame
df = pd.read_csv(obj)

print(df)