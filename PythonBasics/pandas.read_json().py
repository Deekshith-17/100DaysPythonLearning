import pandas as pd
from io import StringIO

# Create a string representing JSON data
data = """[
    {"Name": "Braund", "Gender": "Male", "Age": 30},
    {"Name": "Cumings", "Gender": "Female", "Age": 25},
    {"Name": "Heikkinen", "Gender": "Female", "Age": 35}
]"""

# Use StringIO to convert the JSON formatted string data into a file-like object
obj = StringIO(data)

# Read JSON into a Pandas DataFrame
df = pd.read_json(obj)

print(df)