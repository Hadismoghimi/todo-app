def print_shape(rows, columns):
    for i in range(rows):
        if i == 0 or i == rows - 1:
            print('*' * columns)
        else:
            print('*' + ' ' * (columns - 2) + '*')
rows = input("tedad satr ra vared konid: ")
rows = int(rows)
columns =input("tedad setun ra vared konid: ")
columns = int(columns)
print_shape(rows, columns)

# n=input("Enter a number: ")
# n=int(n)

# for i in range(0,n):
#     for j in range(0,i):
#         print(" ",end="")
# for in range(0,n):
#     print(" ",end="")
# print()
