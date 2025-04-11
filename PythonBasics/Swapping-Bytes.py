import numpy as np 
a = np.array([1, 256, 8755], dtype = np.int16) 

print ('Our array is:', a)

print ('Representation of data in memory in hexadecimal form:', map(hex,a))
# We can see the bytes being swapped
print ('Applying byteswap() function:', a.byteswap())
print ('In hexadecimal form:', map(hex,a))