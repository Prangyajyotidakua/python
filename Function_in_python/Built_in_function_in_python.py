#find the absolute value
num= -100
print(abs(num)) #100


"""The all() function in Python is a built-in 
function that takes an iterable 
(such as a list, tuple, or any other iterable) 
as its argument and returns True if all elements 
in the iterable are considered "truthy," and False
 otherwise. If the iterable is empty, the all() 
 function also returns True since there are no 
 elements to check."""
lst=[1,2,3,4,5]
print(all(lst)) #true

# Example 1: All elements in the list are truthy
my_list1 = [True, 1, "hello", 42]
result1 = all(my_list1)
print(result1)  # Output: True

# Example 2: At least one element is falsy (0)
my_list2 = [True, 1, "hello", 0]
result2 = all(my_list2)
print(result2)  # Output: False

# Example 3: Empty iterable (always evaluates to True)
empty_list = []
result3 = all(empty_list)
print(result3)  # Output: True