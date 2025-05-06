#Assignment No-21:
#Create a class Countdown that takes a start number. 
#Implement __iter__() and __next__() to make the object iterable in a for-loop, 
# counting down to 0.

class Countdown:
    def __iter__(self): #iter:-This method is automatically called at the start of a for loop.
        self.curr = 10 #curr:-This is an instance variable that stores the current countdown value.
        return self
    
    def __next__(self):
        if self.curr > 0:
            self.curr -= 1
            return self.curr
        else:
            raise StopIteration #
    
for i in Countdown():
    print(i)