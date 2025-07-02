class A:
    def __init__(self, name: str):
        self.name = name

    def do_something(self):
        return "This is class A"

class B(A): #it will inherit the init above from this parent class 'A'
    def do_something(self):
        return "This is class B"

class C(A):
    def do_something(self):
        return "This is class C"

class D(B, C): pass #inherits all the parents classes above

d = D("D") #object
print(d.do_something()) #first it will check its own class D
# then its pass so it goes to its parent class and the first is 'B'
#then it goes to class B and returns what class B has
#if class B also has pass it will go look in class C
#if class C also has pass it will go and look in the parent of the classes until it finds something
print(D.mro())
