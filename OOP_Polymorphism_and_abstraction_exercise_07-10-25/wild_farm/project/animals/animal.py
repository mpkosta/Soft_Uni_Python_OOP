from abc import ABC, abstractmethod

from project.food import Food


class Animal(ABC):
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @property
    @abstractmethod
    def allowed_food(self) -> list[Food]:
        pass

    @property
    @abstractmethod
    def weight_addition_by_animal_type(self) -> float:
        pass


    @staticmethod
    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food: Food):
        if type(food) not in self.allowed_food:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * self.weight_addition_by_animal_type
        self.food_eaten += food.quantity
        return None


class Bird(Animal, ABC):
    def __init(self, name, weight, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"

class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}]"