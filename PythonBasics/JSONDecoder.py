import json

data = ['Rakesh', {'marks': (50, 60, 70)}]
e = json.JSONEncoder()
s = e.encode(data)
d = json.JSONDecoder()
obj = d.decode(s)
print(obj, type(obj))