def functionA():
   counter =0
   def functionB():
      nonlocal counter
      counter+=1
      return counter
   return functionB

myfunction = functionA()

retval = myfunction()
print ("Counter:", retval)

retval = myfunction()
print ("Counter:", retval)

retval = myfunction()
print ("Counter:", retval)