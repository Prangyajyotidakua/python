"""
the super() function is used to call a method from a parent or superclass within a subclass. It is particularly useful when you want to extend or override the behavior of a method in the parent class while still using the functionality provided by that method in the parent class. super() allows you to invoke the method of the parent class explicitly."""

class Parent:
    def __init__(self,name):
        self.name= name
    def say_hello(self):
        print(f"hello {self.name}") 
class Child(Parent):
    def __init__(self,name,age):
        super().__init__(name) #call the parent class constructor
        self.age=age
    def say_hello(self):
        super().say_hello() #call the parent class method
        print(f"and your age is {self.age}")

p= Child('Lisa' ,21)   
p.say_hello()                