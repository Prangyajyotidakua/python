my_list = ['one', 'two', 'four']
my_list.insert(2, "three")
print(my_list)


list1 = ['one', 'two', 'three', 'four']
list2 = ['five', 'six']
list1.extend(list2)
print(list1)

my_list = ["one", "two", "three", "four"]
my_list.remove("four")
print(my_list)

my_list = ["one", "two", "three", "four"]
length = len(my_list)
print(length)


my_list = []
my_list.append("one")
my_list.append("two")
my_list.append("three")
my_list.append("four")
print(my_list)

my_list = ["apple", "banana", "cherry", "date"]

# Remove and return the element at index 2 (which is "cherry")
removed_element = my_list.pop(2)

print("Removed Element:", removed_element)
print("Updated List:", my_list)


list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Append list2 as a single element to list1
list1.append(list2)

print(list1)
#[1, 2, 3, [4, 5, 6]]

lst = ['one', 'two', 'three', 'four']


if 'two' in lst:
     print('Chintu')

#keyword 'not' can combined witth 'in

if 'six' not in lst:
    print('Mintu')





#reverse the entire List 1st = ['one', 'two', 'three', 'four']

# 1st.reverse() print(1st)

# ['four', 'three', 'two', 'one']