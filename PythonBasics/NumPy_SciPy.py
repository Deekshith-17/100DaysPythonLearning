def fibonacci(n):
   """
   Compute the nth Fibonacci number.

   Parameters
   ----------
   n : int
      The index of the Fibonacci number to compute.

   Returns
   -------
   int
      The nth Fibonacci number.

   Examples
   --------
   >>> fibonacci(0)
   0
   >>> fibonacci(5)
   5
   >>> fibonacci(10)
   55
   """
   if n == 0:
      return 0
   elif n == 1:
      return 1
   else:
      return fibonacci(n-1) + fibonacci(n-2)
	  
result = fibonacci(4)
print("Result:", result)	  