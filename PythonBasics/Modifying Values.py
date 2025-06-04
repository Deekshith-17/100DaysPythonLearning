import pandas as pd
s = pd.Series([1,2,3,4,5])

# Display the original series 
print("Original Series:\n",s)

# Modify the values of first two elements
s[:2] = [100, 200]

print("Series after modifying the first two elements:",s)