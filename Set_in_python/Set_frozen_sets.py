"""
add or remove elements from a frozen set.

Hashable: Frozen sets are hashable, which means they can be used as keys in dictionaries and elements in other sets. This is because their contents cannot change, ensuring a consistent hash value.

Unordered: Like regular sets, frozen sets are unordered collections of unique elements. This means they do not have a specific order, and you cannot access elements by their index.

Syntax: Frozen sets are created using the frozenset() constructor or by using curly braces {} with elements separated by commas."""

# Creating a frozen set
fs = frozenset([1, 2, 3, 4, 5])

# Accessing elements (no indexing)
for element in fs:
    print(element)

# Using a frozen set as a dictionary key
my_dict = {fs: "Frozen Set Example"}

# Hashing works because frozen sets are immutable
print(hash(fs)) 

set1 = frozenset([1,2,3,4])
set2 = frozenset([3,5,6,4])

# union
print(set1.union(set2))
print(set1 | set2) #frozenset({1, 2, 3, 4, 5, 6})

# intersection
print(set1.intersection(set2))
print(set1 & set2) #frozenset({3, 4})

# symmetric difference
print(set1^set2) # or 
print(set1.symmetric_difference(set2))