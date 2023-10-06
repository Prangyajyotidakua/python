alp01 = 65
for i in range(3):
    for j in range(5):
        if j == 3 or j == 3-i or j==3+i :
            print("A",end='')
        else:
            print(end=" ")  
        
    print()          