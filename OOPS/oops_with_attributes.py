"""
The purpose of self is to access and manipulate
 attributes and methods of the instance within the 
 class.
"""

class Person:
    def set_name(self,name):
        self.name = name
    def set_age(self,age):
        self.age = age
    def set_color(self,color):
        self.color = color
    def set_height(self,height):
        self.height = height 
    def show_person(self):
        print("hello my name is{0},my age is {1},my height is {2},my color is {3}".format(self.name,self.age,self.height,self.color)) 
        print(f"Hello, my name is {self.name}, my age is {self.age}, my height is {self.height}, my color is {self.color}")
        print("Hello, my name is %s, my age is %d, my height is %.2f, my color is %s" % (self.name, self.age, self.height, self.color) )  

p= Person()
p.set_name("lisa")
p.set_age(21)
p.set_color("white")
p.set_height(5.5)
p.show_person()
