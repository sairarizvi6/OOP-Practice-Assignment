#Assignment No-6:
#Create a class Logger that prints a message when an object is created (constructor) 
#and another message when it is destroyed (destructor).

class Logger:
    def __init__(self, message):
        self.message = message
        print(f"Constructor: {self.message}")
    
    def __del__(self):
        print(f"Destructor: {self.message}")
    

l = Logger("Hello Kitty!")
del l
