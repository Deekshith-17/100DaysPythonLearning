import pandas as pd

url ="https://raw.githubusercontent.com/Opensourcefordatascience/Data-sets/master/blood_pressure.csv"

# read CSV into a Pandas DataFrame using the read_table() function
df = pd.read_table(url,sep=',')

print(df.head(5))