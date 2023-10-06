my_name = 'Lisa'
my_name = my_name.lower()
reverse_name = reversed(my_name)
if list(my_name) == list(reverse_name):
    print('name is a pallindrom',my_name)
else:
    print('name is not pallindrom', my_name)    
