# def compute(n):
#     n_str=str(n)
#     nn=int(n_str*2)
#     nnn=int(n_str*3)
#     nnnn=int(n_str*4)
#     return n+nn+nnn+nnnn
# print("Testing the function for n=4:")
# result_4=compute(4)
# print(f"Result:{result_4}")
# print("\n Testing the function for n =7:")
# result_7=compute(7)
# print(f"Result:{result_7}")


def compute(n):
    n_str=str(n)
    nn=int(n_str*2)
    nnn=int(n_str*3)
    nnnn=int(n_str*4)
    return n+nn+nnn+nnnn
n=int(input("Enter the function for n:"))
result_1=compute(n)
print(f"Result:{result_1}")
n=int(input("Enter the function for n:"))
result_2=compute(n)
print(f"Result:{result_2}")