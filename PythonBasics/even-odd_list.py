evenlist=[]
oddlist=[]
for i in range(20):
    num=int(input(f"Enter Number{i+1}:"))
    if num%2==0:
        evenlist.append(num)
    else:
        oddlist.append(num)
print("\n Even Numbers:",evenlist)
print("\n Odd Numbers:",oddlist)
print(f"\n Number of even numbers:{len(evenlist)}")
print(f"\n Number of odd numbers:{len(oddlist)}")