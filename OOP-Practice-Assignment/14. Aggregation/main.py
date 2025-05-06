#Assignment No-14:
#Create a class Department and a class Employee. 
#Use aggregation by having a Department object store a reference to an Employee object
# that exists independently of it.

#Aggregation = A "has-a" relationship where one object contains references to other independent objects.

class Department:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def __str__(self):
        return f"Name: {self.name}, Department: {self.department.name}"

department = Department("IT")
employee = Employee("Ahmed", department) #Aggregation: An Employee "has a" Department, but both can exist independently.

print(employee)