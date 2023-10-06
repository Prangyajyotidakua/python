squares = {2:4 , 3:9 ,4:16 ,5 :15 , 6:36}
my_dict= squares.copy() #dict_keys([2, 3, 4, 5, 6])
print(my_dict) #{2:4 , 3:9 ,4:16 ,5 :15 , 6:36}
print(squares.items()) #dict_items([(2, 4), (3, 9), (4, 16), (5, 15), (6, 36)])
print(squares.keys()) #show keys
print(squares.values()) #show val



subjects = {}.fromkeys(['Math','English','Hindi'],0)
print(subjects) #'Math': 0, 'English': 0, 'Hindi': 0}


d ={} #empty dictionary
print(dir(d)) #show all the function of dictionary
