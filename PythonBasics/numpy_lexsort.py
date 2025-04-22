import numpy as np 

# Define keys
nm = ('raju', 'anil', 'ravi', 'amar') 
dv = ('f.y.', 's.y.', 's.y.', 'f.y.') 

# Get indices for sorted order
ind = np.lexsort((dv, nm))

print("Applying lexsort() function:",ind)

# Use indices to get sorted data
print("Use this index to get sorted data:",[nm[i] + ", " + dv[i] for i in ind]) 