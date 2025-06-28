class Worker:
    """
    A worker class that gives description of employees
    and their salaries
    """
    salary = 3000 #class attribute that is shared by all objects in the class


    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name #data attributes
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name} is an employee for Coca-Cola that earns ${self.salary} USD'

    def __repr__(self):
        return f"Worker({repr(self.first_name)}, {self.last_name!r})" #repr() or '!r' to use the represent method 

worker1 = Worker(first_name="John", last_name="Smith")
worker2 = Worker(first_name="Sarah", last_name="Mckenzey")
print(worker1.first_name)
print(worker2.first_name)
print(worker1.salary)
print(worker2.salary)
Worker.salary = 3500
worker1.salary = 4000
print(worker1.salary)
print(worker2.salary)
print(worker1.__dict__) #returns info as dictionary
print(worker2.__dict__)
print(worker1.__doc__) #returns doc of the class
print(str(worker1))
print(repr(worker1)) #str methodd uses repr method as a fallback