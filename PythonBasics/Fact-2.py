def recur_factorial(n):
    if n==1:
        return n
    else:
        return n*recur_factorial(n-1)
Num=int(input("Enter a Number:"))
if Num<0:
    print("Sorry,factorial does not exist for negative numbers")
elif Num==0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of",Num,"is",recur_factorial(Num))