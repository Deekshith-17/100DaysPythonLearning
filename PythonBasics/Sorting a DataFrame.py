import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame({'col1':[2,9,5,0],'col2':[1,3,2,4]})
print("Original DataFrame:\n", unsorted_df)

# Sort the DataFrame by values
sorted_df = unsorted_df.sort_values(by='col1')
print("\nOutput Sorted DataFrame:\n", sorted_df)