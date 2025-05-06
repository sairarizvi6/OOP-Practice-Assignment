#Assignment No-13:
#Create a class Engine and a class Car. 
#Use composition by passing an Engine object to the Car class during initialization. 
#Access a method of the Engine class via the Car class.

# Composition = The composed object has control over its components, which cannot exist on their own
# "has-a" relationship

class Engine:
    def start(self):
        return "Engine started."

class Car:
    def __init__(self):
        self.engine = Engine()# Composition: A Car contains an Engine.

my_car = Car()
print(my_car.engine.start())

