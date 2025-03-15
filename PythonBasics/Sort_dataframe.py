import pandas as df
Data={
    "Name":["Arjun","David","Charlie","Anuj","Naman"],
    "Age":[24,27,22,32,29],
    "City":["Bengaluru","Delhi","Mumbai","Udupi","Mangaluru"]
}
df=df.DataFrame(Data)
df_sorted=df.sort_values(by="Age",ascending=False)
print("Data Frame sorted by Age in descending order:")
print(df_sorted)
