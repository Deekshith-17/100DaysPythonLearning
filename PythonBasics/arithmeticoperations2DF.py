import pandas as pd

# Create two DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})
df2 = pd.DataFrame({'A': [10, 20, 30], 'B': [50, 60, 70]}, index=[1, 2, 3])

# Display the input DataFrames
print("DataFrame 1:\n", df1)
print("\nDataFrame 2:\n", df2)

# Perform arithmetic operations
print("\nAddition of Two DataFrames:\n", df1 + df2)
print("\nSubtraction of Two DataFrames:\n", df1 - df2)
print("\nMultiplication of Two DataFrames:\n", df1 * df2)
print("\nDivision of Two DataFrames:\n", df1 / df2)