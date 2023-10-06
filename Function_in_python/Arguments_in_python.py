# Keyword Arguments:
def subtract(a, b):
    return a - b

result = subtract(b=5, a=3)  # Using keyword arguments to specify 'a' and 'b'.
print(result)  # Output: -2


# Positional Arguments:
def add(a, b):
    return a + b

result = add(3, 5)  # Here, 3 is assigned to 'a' and 5 is assigned to 'b'.
print(result)  # Output: 8


# Default Arguments:
def greet(name="Guest"):
    return f"Hello, {name}!"

message = greet()  # No argument provided, so 'name' defaults to "Guest".
print(message)  # Output: "Hello, Guest!"


"""
**Variable-Length Keyword Arguments (kwargs):
**kwargs allows a function to accept a variable number of keyword arguments.
These arguments are collected into a dictionary.
"""
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York



"""
arbitrary arguments:
*Variable-Length Positional Arguments (args):
*args allows a function to accept a variable number of positional arguments.
These arguments are collected into a tuple.
"""
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

result = sum_all(1, 2, 3, 4, 5)
print(result)  # Output: 15



"""Positional Arguments Followed by Keyword Arguments:
You can use a combination of positional and keyword arguments in a function call, but positional arguments must come before keyword arguments.
"""
def example(a, b, c=0, d=1):
    return a + b + c + d

result = example(1, 2, d=4)  # Positional arguments '1' and '2', keyword argument 'd'.
print(result)  # Output: 7

