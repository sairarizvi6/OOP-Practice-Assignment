#Assignment No-2:
#Create a class Counter that keeps track of how many objects have been created. 
#Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0

    @classmethod
    def display_count(cls):
        cls.count += 1
        return cls.count
    

print(Counter.display_count())
print(Counter.display_count())