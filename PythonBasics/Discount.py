discount = 0
amount = int(input("Enter Price:"))
# Check he amount value
if amount > 1000:
   discount = amount * 10 / 100

print("amount = ", amount - discount)