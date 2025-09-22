def fibonacci(n):
    if n <= 0:
        return 0  # Base case for n = 0
    elif n == 1:
        return 1  # Base case for n = 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case
        
fib_series = [fibonacci(i) for i in range(6)]
print(fib_series)