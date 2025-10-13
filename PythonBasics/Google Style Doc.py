def divide(dividend, divisor):
   """
   Divide two numbers and return the result.

   Args:
      dividend (float): The number to be divided.
      divisor (float): The number to divide by.

   Returns:
      float: The result of the division.

   Raises:
      ValueError: If `divisor` is zero.
   """
   if divisor == 0:
      raise ValueError("Cannot divide by zero")
   return dividend / divisor

result = divide(4, 7)
print("Division:", result)