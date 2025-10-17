import json

data = ['Rakesh', {'marks': (50, 60, 70)}]
e = json.JSONEncoder()

# Using iterencode() method 
for obj in e.iterencode(data):
   print(obj)