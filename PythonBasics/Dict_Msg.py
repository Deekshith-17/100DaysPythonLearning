Students= {
    101:"Ajay",
    102:"Vineet",
    103:"Sanjay",
    104:"Neha",
    105:"Riya"
}
Roll_number=int(input("Enter the roll number:"))
if Roll_number in Students:
    print(f"Congratulations {Students[Roll_number]}!")
else:
    print("Congratulations Student!")
    