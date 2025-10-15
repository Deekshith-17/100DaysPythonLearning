import json

# JSON string
json_string = '{"name": "John", "age": 30, "is_student": false, "courses": ["Math", "Science"], "address": {"city": "New York", "state": "NY"}}'

# Deserialize JSON string to Python object
python_obj = json.loads(json_string)

print(python_obj)