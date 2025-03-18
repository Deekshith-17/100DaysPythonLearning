# a = 10
# b = 20
# list = [1, 2, 3, 4, 5 ]

# print ("a:", a, "b:", b, "list:", list)

# if ( a in list ):
#    print ("a is present in the given list")
# else:
#    print ("a is not present in the given list")

# if ( b not in list ):
#    print ("b is not present in the given list")
# else:
#    print ("b is present in the given list")

# c=b/a
# print ("c:", c, "list:", list)
# if ( c in list ):
#    print ("c is available in the given list")
# else:
#     print ("c is not available in the given list")
    
    
    
fruits = ["apple", "banana", "mango", "grape"]
fruit_to_check = input("Enter the name of a fruit: ")
if fruit_to_check in fruits:
    print(f"{fruit_to_check} is in the list of fruits.")
else:
    print(f"{fruit_to_check} is not in the list of fruits.")
if fruit_to_check not in fruits:
    print(f"{fruit_to_check} is not a part of the fruits collection.")
