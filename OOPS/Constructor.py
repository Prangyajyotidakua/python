# constructor use to intializes the object
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display_info(self):
        print(f"Name : {self.name}, Age:{self.age}")


p1=Person('lisa',21)
p2=Person('Prangya',21)  
p1.display_info()          
p2.display_info()          