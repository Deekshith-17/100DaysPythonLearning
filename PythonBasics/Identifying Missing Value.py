import numpy as np 

# Creating a 2D array with NaN values
arr_2d = np.array([[1.0, np.nan, 3.5],
                   [np.nan, 5.1, 6.3]])

# Identifying NaN values in the 2D array
nan_mask_2d = np.isnan(arr_2d)

print("Original 2D Array:\n", arr_2d)
print("NaN Mask 2D:\n", nan_mask_2d)