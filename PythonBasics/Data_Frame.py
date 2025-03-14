import pandas as pd
data={
    "Name":["Arjun","David","Charlie","Anuj","Naman"],
    "Age":[24,27,22,32,29],
    "City":["Bengaluru","Delhi","Mumbai","Udupi","Mangaluru"]
}
df=pd.DataFrame(data)
print("First few rows of the Data Frame :")
print(df.head())
print("\n Basics information of the Data Frame :")
df.info()
print("\n Summary statistics of the Data Frame :")
print(df.describe())
