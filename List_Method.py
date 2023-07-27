num = [3,8,2,0,32,23,34,3,3,3]
# append at the end only
num.append(20)

# insert is give the permission to add at specific location
num.insert(4,56)

# remove will remove the item
num.remove(0)

# pop will always remove the last item in the list 
num.pop()

# index is show the inex number of the given example
print(num.index(8))

# the value is present or not true or false 
print(90 in num)

# count will count the redundancy
print(num.count(3))

# sorting purpose we use sort method
num.sort()

# reverse a string
num.reverse()

print(num)

# copy method will copy a list these are 2 independent list
num2 = num.copy()
print(num2)