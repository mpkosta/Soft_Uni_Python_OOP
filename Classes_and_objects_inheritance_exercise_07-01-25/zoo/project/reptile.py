from project.animals.animal import Animal


class Reptile(Animal):
    def __init__(self, name: str):
        super().__init__(name) #or just a pass it will still work