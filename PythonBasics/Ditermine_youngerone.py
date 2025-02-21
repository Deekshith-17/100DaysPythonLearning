R=int(input("Enter the age of Ram:"))
S=int(input("Enter the age of Shyam:"))
A=int(input("Enter the age of Ajay:"))
if(R<S and S<A):
    print("Ram is younger than Shyam and Ajay")
elif(S<R and R<A):
    print("Shyam is younger than Ram and Ajay")
elif(A<S and S<R):
    print("Ajay is younger than Shyam and Ram")