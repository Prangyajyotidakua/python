d = {'a':1 ,'b':2 , 'c':3}
for pair in d.items():
    print(pair)

"""
('a', 1)
('b', 2)
('c', 3)
"""    

new = {k:v for k,v in d.items() if v>2} #('c', 3)

new2 = {k+'m' : v*2 for k ,v in d.items()}
print(new2) #{'am': 2, 'bm': 4, 'cm': 6}