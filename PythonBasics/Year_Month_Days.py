n=int(input("Enter days:"))
y=n//365
m=(n-365*y)//30
d=n-365*y-m*30
print("years:",y)
print("month:",m)
print("days:",d)