sum=0
n=int(input("Enter the number is:"))
org=n
while(n!=0):
    rem=n%10
    sum=sum*10+rem
    n=n//10
    if(org==sum):
        print("Palindrom")
    else:
        print("Not Palindrome")