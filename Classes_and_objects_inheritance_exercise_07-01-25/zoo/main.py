from project.lizard import Lizard
from project.mammal import Mammal

mammal = Mammal("Stella")
# print(mammal.__class__.__bases__[0].__name__)
# print(mammal.name)
# lizard = Lizard("John")
# print(lizard.__class__.__bases__[0].__name__)
# print(lizard.name)

print(mammal) #it will return location of object somewhere in the RAM
print(mammal.__class__) # it returns only the class
print(mammal.__class__.__bases__) #looks for the parents and hierarchy
b = Bear("Mimi")
print(b.__class__.__bases__[0]) #we get the first parents(naslednik)

