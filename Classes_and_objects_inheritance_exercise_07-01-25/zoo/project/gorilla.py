from project.animals.mammals import Mammal


class Gorilla(Mammal):
    def __init__(self, name: str):
        super().__init__(name)