import numpy as np

# Create a NumPy array
array = np.array([10, 15, 20, 25, 30, 35])

# Define a custom function for filtering
def is_prime(num):
   """Return True if num is a prime number, False otherwise."""
   if num <= 1:
      return False
   for i in range(2, int(np.sqrt(num)) + 1):
      if num % i == 0:
         return False
   return True

# Apply the function to each element of the array
mask = np.array([is_prime(x) for x in array])

# Use the mask to filter the array
filtered_array = array[mask]

print("Original Array:", array)
print("Mask (prime numbers):", mask)
print("Filtered Array (prime numbers):", filtered_array)                                