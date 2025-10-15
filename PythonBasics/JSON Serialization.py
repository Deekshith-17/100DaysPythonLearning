import json

# Python dictionary
data = {"name": "Alice", "age": 30, "city": "New York"}

# Serialize to JSON string
json_string = json.dumps(data)
print(json_string)