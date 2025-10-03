import json

# Create a dictionary
data = {"name": "Alice", "age": 25, "city": "San Francisco"}

# Serialize the dictionary and write it to a file
with open("data.json", "w") as f:
   json.dump(data, f)
   print ("Success!!")