def rsum(num):
    if num!=0:
        digit=num%10
        num=int(num/10)
        sum=digit+rsum(num)
    else:
        return 0
    return sum
n=int(input("Enter number:"))
rs=rsum(n)
print("Sum of digits=",rs)
