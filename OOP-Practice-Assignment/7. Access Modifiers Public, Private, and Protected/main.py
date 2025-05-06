#Assignment No-7:
#Create a class Employee with:a public variable name,a protected variable _salary, and
#a private variable __ssn.
#Try accessing all three variables from an object of the class and document what happens.


class Employee:
    def __init__(self, name, salary, ssn): 
        self.name = name
        self._salary = salary
        self.__ssn = ssn #SSN:-(Social Security Number#This is a security measure) 

# Creating a class instance
jobber = Employee("Maisa", '$50000', '123-45-6789')

# Accessing a public attribute
print(jobber.name)
# Accessing a protected attribute
print(jobber._salary)
# Accessing a private attribute via name mangling
print(jobber._Employee__ssn)

# Use getattr() to call a private method
print(getattr(jobber,'_Employee__ssn'))