import pandas as pd

# Import StringIO to load a file-like object for reading CSV
from io import StringIO

# Create string representing CSV data
data = """S.No,Name,Age,City,Salary
1,Tom,28,Toronto,20000
2,Lee,32,HongKong,3000
3,Steven,43,Bay Area,8300
4,Ram,38,Hyderabad,3900"""

# Use StringIO to convert the string data into a file-like object
obj = StringIO(data)
    
# read CSV into a Pandas DataFrame
df = pd.read_csv(obj, skiprows=2)

# Display the DataFrame
print(df)