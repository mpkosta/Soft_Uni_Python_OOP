from project.product import Product


class Food(Product):
    def __init__(self, name: str, quantity=15): #new value of quantity
        super().__init__(name, quantity)