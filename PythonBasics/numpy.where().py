import numpy as np 
x = np.arange(9.).reshape(3, 3) 

print ('Our array is:',x)  

print ('Indices of elements > 3')
y = np.where(x > 3) 
print (y)  

print ('Use these indices to get elements satisfying the condition',x[y])