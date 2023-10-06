"""
a set is an unordered collection of unique elements. Sets are defined using curly braces 
Sets: Sets are unordered collections of elements. They don't have a specific order, and you cannot access elements by their index.

Lists: Lists are ordered collections, and elements in a list are indexed. You can access list elements by their index, and the order of elements in a list is maintained.

Tuples: Tuples are also ordered collections, and like lists, elements are indexed, and the order is preserved.
Duplicates:

Sets: Sets do not allow duplicate elements. If you attempt to add a duplicate value to a set, it will be ignored.

Lists: Lists can contain duplicate elements. You can have the same value appear multiple times in a list.

Tuples: Tuples can also contain duplicate elements, just like lists.

"""

s ={1,2,3,4}
print(s) #{1,2,3,4}
s2 = {1,2,3,4,4}
print(s2) #{1,2,3,4}

s.add(5) # add at rondom place
s.update([5,6,7,1])
s.discard(2) #{1,3,4} it will not throw an error if the element is not present
s.remove(3) #{1,4} it will throw an error if that element is not present
s.pop() # remove random element mostly the front element
s.clear #remove all the items from the set