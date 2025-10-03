import json

# JSON string
json_string = '{"name": "Alice", "age": 25, "city": "San Francisco"}'

# Deserialize the JSON string into a Python dictionary
loaded_data = json.loads(json_string)
print(loaded_data)  