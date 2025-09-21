def functionA(name):
   name ="New name"
   def functionB():
      print (name)
   return functionB
   
myfunction = functionA("My name")
myfunction()