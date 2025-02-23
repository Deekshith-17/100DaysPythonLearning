P=int(input("Enter percentage:"))
if(P>=60):
    print("First division")
elif(P>=50 and P<=59):
    print("Second division")
elif(P>=40 and P<=49):
    print("Third division")
else:
    print("Fail")