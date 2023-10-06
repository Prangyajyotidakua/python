# Dictionary with mixed data types
mixed_dict = {"name": "Alice", 42: "Forty-Two", (1, 2): "Tuple Key"}

# Dictionary with string keys
person = dict(name="John", age=30, city="New York")

# Dictionary with integer keys
grades = dict([(1, "A"), (2, "B"), (3, "C")])


# Dictionary with mixed data types
mixed_dict = dict(name="Alice", num=42, key=("A", "B"))

# Dictionary with tuple keys
contact_book = {("Alice", "Smith"): "alice@example.com", ("Bob", "Johnson"): "bob@example.com"}

# Mixed dictionary example
mixed_dict = {
    "name": "John",
    "age": 30,
    "grades": {1: "A", 2: "B", 3: "C"},
    "city": "New York",
    "is_student": True
}

# create a dictionary with list of tupples
my_dict =dict([(1,'abc'),(2,'xyz')])
print(my_dict) #{1: 'abc', 2: 'xyz'}

# remove element by key
print(mixed_dict.pop('age'))

# remove an arbitary key
print(mixed_dict.popitem())

# remove by delete a particular key
del mixed_dict['city']
print(mixed_dict)

# to remove all the item in the dictionary
print(mixed_dict.clear) #mixed_dict()

# to delete the entire dictionary
del mixed_dict
print(mixed_dict)#name error beacuse dicct is deleted


