n = input("enter a string :")

length = len(n)

for i in range(length):
    for j in range(i+1):
        print(n[j],end="")
    print()   
    