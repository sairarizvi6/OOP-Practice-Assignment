#Assignment No-17:
#Create a class decorator add_greeting that modifies a class to add a greet() method 
#returning "Hello from Decorator!". Apply it to a class Person.

def add_greeting(decorator): # decorator = Person
    def greet(self):
        return "Hello, from decorator!"
    decorator.greet = greet
    return decorator


@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

person1 = Person("Ali")
print(person1.greet())