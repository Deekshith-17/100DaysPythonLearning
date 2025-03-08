BS=int(input("Basic Salary is:"))
if BS>1000:
    hra = BS * 15 /100
    da = BS * 95 / 100
    ca = BS * 10 / 100
else:
    hra = BS * 10 /100
    da = BS * 90 / 100
    ca = BS * 5 / 100
GS=BS+da+hra+ca
print("Gross Salary=RS."+str(GS))