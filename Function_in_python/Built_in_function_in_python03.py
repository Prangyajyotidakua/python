# filter function

def positive_num(num):
    if num > 0:
        return num    
# create a list with numbers from -10 to 10
num_list= range(-10,10)
print(list(num_list)) #[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# filter function require 2 things 1st is name of the function and 2nd is list name
positiveNumList = list(filter(positive_num,num_list))
print(positiveNumList) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

"""------------------------------------------------------------------"""

# isinstance function
lst =[]
print(isinstance(lst,list)) #true
print(isinstance(lst,tuple)) #false

