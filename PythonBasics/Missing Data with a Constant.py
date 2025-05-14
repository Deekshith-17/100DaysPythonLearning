import numpy as np

# Creating an array with NaN values
arr = np.array([1.0, 2.5, np.nan, 4.7, np.nan, 6.2])

# Defining a constant value for imputation
constant_value = 0

# Imputing NaN values with the constant
imputed_arr = np.where(np.isnan(arr), constant_value, arr)

print("Original Array:\n", arr)
print("Constant Value:", constant_value)
print("Imputed Array:\n", imputed_arr)