class Calculator:
   """
   A simple calculator class to perform basic arithmetic operations.

   Methods:
   - add(a, b): Return the sum of two numbers.
   - multiply(a, b): Return the product of two numbers.
   """

   def add(self, a, b):
      """Return the sum of two numbers."""
      return a + b

   def multiply(self, a, b):
      """
      Multiply two numbers and return the result.

      Parameters:
      a (int or float): The first number.
      b (int or float): The second number.

      Returns:
      int or float: The result of multiplying a and b.
      """
      return a * b
	  
cal = Calculator()
print(cal.add(87, 98))
print(cal.multiply(87, 98))