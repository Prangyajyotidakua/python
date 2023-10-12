# Method overriding is a feature in 
# object-oriented programming that allows a
# subclass to provide a specific implementation
# for a method that is already defined in its parent 
# class. 

# Base class (parent class)
class Shape:
    def area(self):
        pass

# Subclass (child class) overriding the area method
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Subclass (child class) overriding the area method
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Create instances of the subclasses
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Call the area method on the instances
print("Circle Area:", circle.area())       # Output: Circle Area: 78.5
print("Rectangle Area:", rectangle.area()) # Output: Rectangle Area: 24

