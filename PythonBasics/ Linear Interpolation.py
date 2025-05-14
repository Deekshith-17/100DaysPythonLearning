import numpy as np
from scipy import interpolate

# Creating an array with NaN values
arr = np.array([1.0, np.nan, 3.5, np.nan, 5.0])

# Interpolating missing values
nans, x = np.isnan(arr), lambda z: z.nonzero()[0]
arr[nans] = np.interp(x(nans), x(~nans), arr[~nans])

print("Original Array:\n", arr)
print("Array with Interpolated Values:\n", arr)