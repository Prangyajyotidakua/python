num = [1,2,3, 1,2,3,4,5,6,7]
num2 =[]
for x in num:
    if x not in num2 :
        num2.append(x)
print(num2)        