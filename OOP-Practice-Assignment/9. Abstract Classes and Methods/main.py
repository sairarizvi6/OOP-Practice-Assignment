#Assignment No-9:
#Use the abc module to create an abstract class Shape with an abstract method area(). 
#Inherit a class Rectangle that implements area().

# Importing ABC and abstract method from abc module. ABC is an abstract base class and abstract method is a decorator that is used to define an abstract method.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self, length, width):
        pass

class Rectangle(Shape):
    def area(self, length, width):
        return length * width 

rec = Rectangle() # Instantiating the class Rectangle() and storing it in rec variable.
area = rec.area(20, 30) # Calling the area method on rec object and passing length and width as arguments.
print(area)

def calculate_area(shape: Shape, length, width):
    return shape.area(length, width)

print(calculate_area(Rectangle(), 20, 30))