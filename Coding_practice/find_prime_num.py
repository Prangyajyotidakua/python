from math import *
def fun(n):
    if n== 0 or n ==1:
        return False
    if n == 2 or n == 3:
        return True
    if n%2==0 or n %3==0:
        return False
    for i in range(5,int(sqrt(n)+1)):
        if n%i == 0 or n %(i+2)==0:
            return False
    return True

t = int(input())
while t:
    n= int(input())
    print(fun(n))
    t=t- 1
    

