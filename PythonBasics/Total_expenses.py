P=int(input("Enter price per item:"))
Q=int(input("Enter quantity:"))
if(Q>1000):
    totalexp=(P*Q)-((P*Q)*10/100)
    print("Total Exp is:",totalexp)
else:
    print("Total Exp is:",P*Q)
