ms=input("Enter 'ma' for married and 'um' for unmarried :")
g=input("Enter 'm' for male and 'f' for female :")
age=int(input("Enter age is:"))
if(ms=='ma'):
    print("Insured")
elif(ms=='um' and g=='m' and age>30):
    print("Insured")
elif(ms=='um' and g=='f' and age>25):
    print("Insured")
else:
    print("Not Insured")