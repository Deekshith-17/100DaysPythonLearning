n = int(input("Enter a number(or 0 to stop): "))
even = 0
odd = 0
while n != 0:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
    n = int(input("Enter another number(or 0 to stop) : "))
print("Total even numbers:", even)
print("Total odd numbers:", odd)