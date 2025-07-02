class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: float = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION #call from self because if it is Vehicle. - then all inherits will take the 1.25 setting always

    def drive(self, kilometers: int):
        consumed_fuel = kilometers * self.fuel_consumption
        #distance_travelled ?
        if self.fuel >= consumed_fuel:
            self.fuel -= consumed_fuel