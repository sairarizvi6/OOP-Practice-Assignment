#Assignment No-16:
#Write a decorator function log_function_call that prints "Function is being called" before 
#a function executes. Apply it to a function say_hello().

#Decorator =A decorator is a function that takes another function as input, 
#adds some functionality, and returns it.

def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

@log_function_call
def say_hello():
    return "Hello!"

print(say_hello())