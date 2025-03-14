import numpy as np
array_1d = np.arange(1,13)
array_reshaped =array_1d.reshape(3,4)
array_transposed =array_reshaped.T   
print("1D Array:")
print(array_1d)
print("Reshaped (3,4) Array:")
print(array_reshaped)
print("Transposed Array:")
print(array_transposed)
