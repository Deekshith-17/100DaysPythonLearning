import pandas as pd

# Create a Pandas Series
s = pd.Series([10, 20, 30, 40, 50])

# Display the Series
print("Pandas Series:\n", s)

# Perform comparison operations
print("\nLess than 25:\n", s.lt(25))
print("\nGreater than 25:\n", s.gt(25))
print("\nLess than or equal to 30:\n", s.le(30))
print("\nGreater than or equal to 40:\n", s.ge(40))
print("\nNot equal to 30:\n", s.ne(30))
print("\nEqual to 50:\n", s.eq(50))