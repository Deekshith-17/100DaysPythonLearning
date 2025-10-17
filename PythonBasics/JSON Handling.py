import json
from datetime import datetime

# Custom deserialization function
def custom_deserializer(dct):
   if 'joined' in dct:
      dct['joined'] = datetime.fromisoformat(dct['joined'])
   return dct

# JSON string with datetime
json_string = '{"name": "John", "joined": "2021-05-17T10:15:00"}'

# Deserialize with custom function
python_obj = json.loads(json_string, object_hook=custom_deserializer)

print(python_obj)