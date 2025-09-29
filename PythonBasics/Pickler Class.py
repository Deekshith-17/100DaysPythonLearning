from pickle import Pickler

# Open a file in binary write mode
with open("data.txt", "wb") as f:
   # Create a dictionary
   dct = {'name': 'Ravi', 'age': 23, 'Gender': 'M', 'marks': 75}
   # Create a Pickler object and write the dictionary to the file
   Pickler(f).dump(dct)
   print ("Success!!")