import numpy as np

# Creating an array with NaN values
arr = np.array([1.0, 2.5, np.nan, 4.7, np.nan, 6.2])

# Calculating the median of non-NaN values
median_value = np.nanmedian(arr)

# Imputing NaN values with the median
imputed_arr = np.where(np.isnan(arr), median_value, arr)

print("Original Array:\n", arr)
print("Median Value:", median_value)
print("Imputed Array:\n", imputed_arr)