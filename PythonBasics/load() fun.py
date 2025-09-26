import pickle

# Open the file in binary read mode
with open('data.pkl', 'rb') as file:
   # Deserialize the data
   data = pickle.load(file)
print(data)