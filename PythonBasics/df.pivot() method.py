import pandas as pd

# Create a DataFrame
df = pd.DataFrame({"Col1": range(12),"Col2": ["A", "A", "A", "B", "B","B", "C", "C", "C", "D", "D", "D"],
"date": pd.to_datetime(["2024-01-03", "2024-01-04", "2024-01-05"] * 4)})

# Display the Input DataFrame
print('Original DataFrame:\n', df)

# Pivot the DataFrame
pivoted = df.pivot(index="date", columns="Col2", values="Col1")

# Display the output
print('Pivoted DataFrame:\n', pivoted)