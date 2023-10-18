from array import *

a1= array('i',[12,32,4534,65,21,97,14])
print(a1)
print(type(a1))
for x in a1:
    print(x)
for x in range(len(a1)):
    print(a1[x],end=' ')    

i=0
while i < len(a1)  :
    print(a1[i],end=' ') 
    i+=1 