import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame({'col1':[2,5,0,1],'col2':[1,3,0,4]})
print("Original DataFrame:\n", unsorted_df)

# Sort the DataFrame 
sorted_df = unsorted_df.sort_values(by='col1' ,kind='mergesort')
print("\nOutput Sorted DataFrame:\n", sorted_df)