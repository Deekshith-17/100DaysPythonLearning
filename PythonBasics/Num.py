num=(int(input("Enter a number:")))
num1=num
reversed_num = 0
while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print("Reversed Number: ",reversed_num)
if (reversed_num==num1):
    print("both are equal")
else:
    print("not equal")