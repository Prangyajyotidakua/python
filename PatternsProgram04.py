n = int(input("enter the value"))
num=0
for i in range(n):
    for j in range(i):
        print(num,end=" ")
        num = num+1
    print()    
    