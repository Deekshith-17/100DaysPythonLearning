def cal_sum_prod(x,y,z):
     SS=x+y+z
     PP=x*y*z
     return SS,PP
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
S,P=cal_sum_prod(a,b,c)
print(S,P)