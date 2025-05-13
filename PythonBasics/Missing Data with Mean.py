import numpy as np

# Creating an array with NaN values
arr = np.array([1.0, 2.5, np.nan, 4.7, np.nan, 6.2])

# Calculating the mean of non-NaN values
mean_value = np.nanmean(arr)

# Imputing NaN values with the mean
imputed_arr = np.where(np.isnan(arr), mean_value, arr)

print("Original Array:\n", arr)
print("Mean Value:", mean_value)
print("Imputed Array:\n", imputed_arr)