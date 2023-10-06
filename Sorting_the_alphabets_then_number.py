str_num = 'A1BK98MHcgoQW'

Alphabet = []
num = []

for i in str_num:
    if i.isalpha():
        Alphabet.append(i)
    elif i.isnumeric():
        num.append(i)  

final = sorted(Alphabet) + sorted(num)
output = ''.join(final)
print(output)

my_str2 = input("enter a string")
al =[]
nu = []
for i in my_str2:
    if i.isnumeric():
        nu.append(i)
    elif i.isalpha():
        al.append(i)
fi = sorted(al)+ sorted(nu)
out = ''.join(fi)
print(out)          