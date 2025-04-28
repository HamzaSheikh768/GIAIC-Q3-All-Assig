# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:
# A with a method show(),
# B and C that inherifrom venv import create
# t from A and override show(),
# D that inherits from both B and C.
# createte an object of D and call show() to observe MRO.

class A:
    def show(self):
        print("A's show method")

class B(A):
    def show(self):
        print("B's show method")

class C(A):
    def show(self):
        print("C's show method")

class D(B, C):
    pass

#____________________________ Example usage
d = D()
d.show()
print(D.__mro__)