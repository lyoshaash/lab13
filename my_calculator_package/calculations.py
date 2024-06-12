from abc import ABC, abstractmethod

class CalculationBase(ABC):
    @abstractmethod
    def calculate_volume(self):
        pass

    @abstractmethod
    def calculate_heat_power(self):
        pass


class RoomCalculation(CalculationBase):
    def __init__(self, length, width, height, num_apartments=1, num_floors=1):
        self.length = length
        self.width = width
        self.height = height
        self.num_apartments = num_apartments
        self.num_floors = num_floors

    def __repr__(self):
        return (f"RoomCalculation(length={self.length}, width={self.width}, height={self.height}, "
                f"num_apartments={self.num_apartments}, num_floors={self.num_floors})")

    def __str__(self):
        return (f"Room with dimensions {self.length}x{self.width}x{self.height} m, "
                f"{self.num_apartments} apartments, {self.num_floors} floors")

    def calculate_volume(self):
        return self.length * self.width * self.height * self.num_apartments * self.num_floors

    def calculate_heat_power(self):
        volume = self.calculate_volume()
        return volume * 0.07
