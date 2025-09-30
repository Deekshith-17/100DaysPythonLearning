import json

# Create a dictionary
data = {"name": "Alice", "age": 25, "city": "San Francisco"}

# Serialize the dictionary to a JSON string
json_string = json.dumps(data)
print(json_string)  