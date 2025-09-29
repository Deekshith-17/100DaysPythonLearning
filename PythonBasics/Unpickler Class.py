from pickle import Unpickler

# Open the file in binary read mode
with open("data.txt", "rb") as f:
   # Create an Unpickler object and load the dictionary from the file
   dct = Unpickler(f).load()
   # Print the dictionary
   print(dct)