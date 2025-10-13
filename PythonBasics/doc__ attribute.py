# Define a function with a docstring
def add(a, b):
    """
    Adds two numbers together.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of a and b.
    """
    return a + b
result = add(5, 3)
print("Sum:", result)

# Define another function with a docstring
def multiply(x, y):
    """
    Multiplies two numbers together.

    Parameters:
    x (int): The first number.
    y (int): The second number.

    Returns:
    int: The product of x and y.
    """
    return x * y
result = multiply(4, 7)
print("Product:", result)

# Accessing the docstrings
print(add.__doc__)
print(multiply.__doc__)