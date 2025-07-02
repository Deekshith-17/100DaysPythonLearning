import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame({'col1':[2,1,0,1],'col2':[1,3,4,2]})

print("Original DataFrame:\n", unsorted_df)

# Sort the DataFrame multiple columns by values
sorted_df = unsorted_df.sort_values(by=['col1','col2'])
print("\nOutput Sorted DataFrame:\n", sorted_df)