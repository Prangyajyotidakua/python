"""Key-Value Pairs: A dictionary consists of a set of key-value pairs. Each key is unique within the dictionary, and it maps to a specific value.

Unordered: Dictionaries in Python are unordered, which means that the order of key-value pairs may not be preserved. This is in contrast to lists and tuples, which are ordered collections.

Mutable: Dictionaries are mutable, meaning you can add, modify, or remove key-value pairs after the dictionary is created.

Dynamic: You can add new key-value pairs to a dictionary as needed, and dictionaries can grow or shrink in size dynamically.

Access by Key: You can access the values associated with keys in a dictionary using square brackets [] or the get() method. The key is used as an index to retrieve the corresponding value.

Keys Must Be Hashable: Keys in a dictionary must be hashable, which means they must be of an immutable data type, such as strings, numbers, or tuples (if they contain only hashable elements). Lists and other dictionaries are not hashable and cannot be used as keys.
"""

# Creating a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
# Accessing dictionary
print(person) # {"name": "John","age": 30,"city": "New York"}

# Accessing values
print(person["name"])  # Outputs: "John"
print(person["age"])   # Outputs: 30

# Modifying values
person["age"] = 31

# Adding a new key-value pair
person["job"] = "Engineer"

# Removing a key-value pair
del person["city"]

