n = int(input("enter the value"))

for i in range(n):
    for j in range(n):
        if i == 0 or j == n-1 or j==i :
            print("*",end='')
        else:
            print(end=" ")  
        
    print()          