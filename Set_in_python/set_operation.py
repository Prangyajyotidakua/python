set1 = {1,2,3,4,5}
set2 = {1,2,3,4,5,6,7,8,8,9}
# union of 2 set using | operator
print(set1|set2)
# or union
print(set1.union(set2))


# intersection using & operator
print(set1 & set2)
print(set1.intersection(set2))

# difference
print("Difference:", set2 - set1)

# symmetric difference it remove the common element in set1 and set2
print(set1^set2)

x= {'a', 'b' ,'c', 'd','e'}
y={'c','d'}
# subset
print("x is subset of y",x.issubset(y)) #False
print("y is subset of x",y.issubset(x))  #true