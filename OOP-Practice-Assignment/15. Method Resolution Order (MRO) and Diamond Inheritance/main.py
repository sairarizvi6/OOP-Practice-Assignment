#Assignment No-15:
#Create four classes:
#A with a method show(),
#B and C that inherit from A and override show(),
#D that inherits from both B and C.
#Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        print("Show method from A")

class B(A):
    def show(self):
        print("Show method from B")

class C(A):
    def show(self):
        print("Show method from C")

class D(B, C):
    pass

d = D()
print("\n")
print(d.show())

# Prints the method resolution order of D.
print(D.mro()) # Show B
