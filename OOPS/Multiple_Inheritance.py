# Base class A
class A:
    def method_A(self):
        print("Method from class A")

# Base class B
class B:
    def method_B(self):
        print("Method from class B")

# Derived class C inherits from both A and B
class C(A, B):
    def method_C(self):
        print("Method from class C")

# Create an instance of class C
obj = C()

# Call methods from both class A and class B
obj.method_A()  # Output: Method from class A
obj.method_B()  # Output: Method from class B

# Call method from class C
obj.method_C()  # Output: Method from class C
