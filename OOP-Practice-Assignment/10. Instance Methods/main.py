#Assignment No-10:
#Create a class Dog with instance variables name and breed. 
#Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} is of a {self.breed} breed. yip!"
    
my_dog = Dog("dog", "Poodle")
print(my_dog.bark())