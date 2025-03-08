num=int(input("Enter a number:"))
flag=False
if (num==1):
    print("Not a prime number")
elif(num>1):
    for i in range(2,num):
        if(num%i==0):
            flag=True
            break
    if flag:
        print("Not a prime number")
    else:
        print("prime number")
else:
    print("Invalid input. Please enter a positive integer.")


