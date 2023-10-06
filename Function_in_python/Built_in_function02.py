# return all the function
nums=[]
print((dir(nums)))

# print quotient and remainder as a tuple
print(divmod(9,2)) #(4,1)

# enumerate(number,start=0)
numbers =[10,20,30,40,50]
for index ,num in enumerate(numbers,10):
    print('index {0} has value {1}'.format(index,num)) 
""" index 10 has value 10
index 11 has value 20
index 12 has value 30
index 13 has value 40
index 14 has value 50"""    

numbers =[10,20,30,40,50]
for index ,num in enumerate(numbers):
    print('index {0} has value {1}'.format(index,num)) 
""" index 10 has value 10
index 0 has value 20
index 1 has value 30
index 2 has value 40
index 3 has value 50"""    