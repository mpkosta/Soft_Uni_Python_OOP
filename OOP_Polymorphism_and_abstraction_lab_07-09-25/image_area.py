class ImageArea:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def get_area(self) -> int:
        return self.width * self.height

    def __eq__(self, other) -> bool:
        return self.get_area() == other.get_area()

    def __gt__(self, other) -> bool:
        return self.get_area() > other.get_area()

    def __ge__(self, other) -> bool:
        return self.get_area() >= other.get_area()

i1 = ImageArea(5, 5)
i2 = ImageArea(2, 2)
print(i1 <= i2)