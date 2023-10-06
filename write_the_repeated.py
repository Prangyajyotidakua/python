my_str = 'avnh12bjewfg9fjcnu933y7teyqni0938r7vw'
num = int(input("enter the number"))
empty_list = []
# print(len(my_str))
for i in my_str:
    if i not in empty_list:
        empty_list.append(i)

print(empty_list)
   


