def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))
nterms =int(input("Enter Number of Terms:"))
if nterms <=0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci Sequence:")
    for i in range(nterms):
        print(recur_fibo(i))
            