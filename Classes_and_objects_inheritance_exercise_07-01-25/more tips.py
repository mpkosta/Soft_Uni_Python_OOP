class A:
    def __init__(self):
        print("Start of class A __init__")
        print("End of class A __init__")

class B(A):
    def __init__(self):
        print("Start of class B __init__")
        super().__init__()
        print("End of class B __init__")

class C(A):
    def __init__(self):
        print("Start of class C __init__")
        super().__init__()
        print("End of class C __init__")

class D(B, C):
    def __init__(self):
        print("Start of class D __init__")
        super().__init__()
        print("End of class D __init__")

d = D()
print(D.mro())
print(d.__class__.__mro__)