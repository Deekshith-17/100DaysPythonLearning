n=int(input("Enter number:"))
def factorial(n):
    fact=1
    while(n>0):
        fact=fact*n
        n=n-1
    return fact
fact=factorial(n)
print("Factorial of the number is:",fact)