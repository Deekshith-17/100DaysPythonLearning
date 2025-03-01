S1=int(input("Enter the size of S1 :"))
S2=int(input("Enter the size of S2 :"))
S3=int(input("Enter the size of S3 :"))
if(S1==S2==S3):
    print("Equilateral triangle")
elif(S1==S2 or S1==S3 or S2==S3):
    print("Isosceles triangle")
else:
    print("Scalene triangle")
    