from math import *

def fun(n):
    d = set()
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return list(d)

result = fun(12)
print(result)
