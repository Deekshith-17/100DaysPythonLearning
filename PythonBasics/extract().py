import numpy as np

array = np.array([10, 20, 30, 40, 50])
condition = array > 25
extracted_elements = np.extract(condition, array)
print("Elements greater than 25:", extracted_elements)