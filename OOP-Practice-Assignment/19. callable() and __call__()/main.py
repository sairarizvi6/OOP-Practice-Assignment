#Assignment No-19:
#Create a class Multiplier with an __init__() to set a factor. 
#Define a __call__() method that multiplies an input by the factor. 
#Test it with callable() and by calling the object like a function.

#*****callable()**** is a built-in function that checks whether an object can be called 
# (used with parentheses () like a function).It returns True***
#******__call__()****** is a special method in Python that makes an object behave like a function.
#If a class has this method, its object can be called using () just like a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor
    
double = Multiplier(5)
triple = Multiplier(5)

print(callable(double)) # True
print(callable(triple)) # True

print(double(2)) # 10
print(triple(3)) # 15