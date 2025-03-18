# a = [1, 2, 3, 4, 5]
# b = [1, 2, 3, 4, 5]
# c = a

# print(a is c)
# print(a is b)

# print(a is not c)
# print(a is not b)



str1 = "hello"
str2 = "hello"
str3 = "world"
if str1 is str2:
    print("str1 and str2 refer to the same memory location.")
if str1 is not str3:
    print("str1 and str3 do not refer to the same memory location.")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
if list1 is not list2:
    print("list1 and list2 are different objects even if they have the same content.")
