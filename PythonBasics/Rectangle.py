l=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
area=l*b
perm=2*l+2*b
if(area>perm):
    print("Area is greater than its perimeter")
else:
    print("Area is not greater than its perimeter")