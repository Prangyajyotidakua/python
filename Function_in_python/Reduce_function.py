# without reduce function
product1 = 1
lst = [1,2,3,4,5]

for num in lst :
    product1*=num
print(product1)  #120 


# with reduce function
from functools import reduce 
def multiply(x,y):
    return x*y
product2 = reduce(multiply,lst) #rolling computation
print(product2) #120

def total_addtion(x,y):
    return x+y
product3 = reduce(total_addtion,lst)
print(product3) #15