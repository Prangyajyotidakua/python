def HCF_of(a,b):
    smaller = b if a>b else a
    hcf=1
    for i in range(1,smaller+1):
        if(a%i==0) and (b%i==0):
            hcf=i
    return hcf
num1=98
num2=78

print('hcf of {num1} and {num2} is',HCF_of(num1,num2)) #2

print("hcf of {0} and {1} is {2}".format(num1,num2,HCF_of(num1,num2)))#hcf of 98 and 78 is 2
        