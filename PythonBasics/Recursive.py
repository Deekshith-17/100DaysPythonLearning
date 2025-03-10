def factorial(x):
    if x==1:
        return 1 
    else:
        return(x*factorial(x-1))
num=int(input("Enter Number:"))
print("The Factorial of Number is:",factorial(num)) 