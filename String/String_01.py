#string are immutable

s = 'hello'
# s[4]='s' #error
del s # delete s 
w = 'hello'
print(w*3) # hello hello hello

l = 'hi'
print(w+ " " + l) # hello hi

count= 0
for i in  'hello world':
    if i == 'l' :
        count+=1
print(count) #3        
print('l' in 'hello world') #True
print('or' in 'hello world') #True