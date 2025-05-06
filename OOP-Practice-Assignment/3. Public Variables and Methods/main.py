#Assignment No-4:
#Create a class Car with a public variable brand and a public method start(). 
#Instantiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return f"{self.brand} is started. Zoom, Zoom!"
    

my_car = Car('Tesla')
print(my_car.brand)
print(my_car.start())