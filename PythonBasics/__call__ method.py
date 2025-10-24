class Multiplier:
   def __init__(self, factor):
      self.factor = factor

   def __call__(self, x):
      return self.factor * x
 
# Create an instance of the Multiplier class
multiply_second_number = Multiplier(2) 

# Call the  Multiplier object to computes factor * x
Result = multiply_second_number(100)  

# Printing result  
print("Multiplication of Two numbers is: ", Result) 