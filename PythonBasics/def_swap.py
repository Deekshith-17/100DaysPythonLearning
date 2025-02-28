def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
a=int(input("Enter a:"))
b=int(input("Enter b:"))
x,y=swap(a,b)
print("a is:",x)
print("b is:",y)