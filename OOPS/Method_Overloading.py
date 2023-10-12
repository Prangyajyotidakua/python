"""
Python does not support method overloading 
in the same way that some other programming 
languages do, such as Java or C++. Method 
overloading refers to the ability to define
multiple methods with the same name in a class,
but with different parameter lists
"""

"""
you can achieve method overloading in
a different way by using default arguments and
variable-length argument lists."""

class MathOperations:
    def add(self, a, b=0, c=0):
        return a + b + c

# Create an instance of the class
math_ops = MathOperations()

# Call the add method with different numbers of arguments
result1 = math_ops.add(1)
result2 = math_ops.add(1, 2)
result3 = math_ops.add(1, 2, 3)

print("Result 1:", result1)  # Output: Result 1: 1
print("Result 2:", result2)  # Output: Result 2: 3
print("Result 3:", result3)  # Output: Result 3: 6
