import numpy as np 
x = np.arange(9.).reshape(3, 3) 

print ('Our array is:',x)  

# define a condition 
condition = np.mod(x,2) == 0 

print ('Element-wise value of condition',condition)

print ('Extract elements using condition',np.extract(condition, x))