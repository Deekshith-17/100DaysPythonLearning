my_tuple=(10,20,30,40,50)
print("Original tuple:",my_tuple)
try:
    my_tuple[1]=100
except TypeError as e:
    print("\n Error",e)
print("\n Tuple after attempting modification:",my_tuple)