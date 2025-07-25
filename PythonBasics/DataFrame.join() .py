import pandas as pd

# Creating the first DataFrame
left = pd.DataFrame({
'id': [1, 2, 3, 4, 5],
'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
'subject_id': ['sub1', 'sub2', 'sub4', 'sub6', 'sub5']
})

# Creating the second DataFrame
right = pd.DataFrame({
'id': [1, 2, 3, 4, 5],
'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
'subject_id': ['sub2', 'sub4', 'sub3', 'sub6', 'sub5']
})

# Merge the DataFrames using the join() method
result = left.join(right, lsuffix='_left', rsuffix='_right')
print(result)