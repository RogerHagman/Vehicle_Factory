from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum

class VehicleType(Enum):
    CAR = 1
    MOTORCYCLE = 2
    BICYCLE = 3

class Vehicle(ABC):
    _total_cost = 0
    _no_of_tires = 0
    
    @property
    @abstractmethod
    def chassis_cost(self) -> float:
        pass
    
    def fit_chassis(self):
        self._total_cost += self.chassis_cost
    
    def fit_tires(self, no_of_tires: int):
        """Fit n tires to the vehicle."""
        self._no_of_tires = no_of_tires
        self._total_cost += self._no_of_tires * self.tire_cost
    
    @abstractmethod
    def assemble_vehicle(self):
        """Assemble the vehicle."""
        pass
    
    @property
    @abstractmethod
    def tire_cost(self) -> float:
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        return self.__class__.__name__
    
    @property
    def total_cost(self):
        return self._total_cost
    
    
class EnginePoweredVehicle(Vehicle, ABC):
    _engine_size = None
    
    @abstractmethod
    def calculate_engine_cost(self, size_cc: int) -> float:
        pass
    
    def fit_engine(self, size_cc: int):
        engine_cost = self.calculate_engine_cost(size_cc)
        self._total_cost += engine_cost
        self._engine_size = size_cc
        print(f"{self.get_name()} engine ({size_cc}cc) cost: {engine_cost:.0f} SEK")


class Car(EnginePoweredVehicle):
    
    def get_name(self) -> str:
        return super().get_name()

    @property
    def chassis_cost(self) -> float:
        return 50_000.00
    
    @property
    def tire_cost(self) -> float:
        return 3000.0
    
    def calculate_engine_cost(self, size_cc: int) -> float:
        return 25_000 + (49.50 * size_cc)
    
    def assemble_vehicle(self):
        self.fit_chassis()
        self.fit_tires(4)
        self.fit_engine(1800)
        print(f"{self.get_name()} assembled with total cost: {self.total_cost:.0f} SEK\n")


class Motorcycle(EnginePoweredVehicle):
    
    def get_name(self) -> str:
        return super().get_name()
    
    @property
    def chassis_cost(self) -> float:
        return 15_000.00
    
    @property
    def tire_cost(self) -> float:
        return 2000.0
    
    def calculate_engine_cost(self, size_cc: int) -> float:
        return 15_000 + (39.50 * size_cc)
    
    def assemble_vehicle(self):
        self.fit_chassis()
        self.fit_tires(2)
        print(f"{self.get_name()} assembled with total cost: {self.total_cost:.0f} SEK\n")

class Bicycle(Vehicle):
    
    def get_name(self) -> str:
        return super().get_name()
    
    @property
    def chassis_cost(self) -> float:
        return 2000.00
    
    @property
    def tire_cost(self) -> float:
        return 800.0
    
    def assemble_vehicle(self):
        self.fit_chassis()
        self.fit_tires(2)
        print(f"{self.get_name()} assembled with total cost: {self.total_cost:.0f} SEK\n")

class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type: VehicleType) -> Vehicle:
        """Factory method to create a vehicle based on the given type."""
        if vehicle_type == VehicleType.CAR:
            return Car()
        elif vehicle_type == VehicleType.MOTORCYCLE:
            return Motorcycle()
        elif vehicle_type == VehicleType.BICYCLE:
            return Bicycle()
        else:
            raise ValueError(f"Vehicle type {vehicle_type} not recognized")

def main():

    factory = VehicleFactory()

    # Create a car
    car = factory.create_vehicle(VehicleType.CAR)
    car.assemble_vehicle()
    print(f"Total cost for {car.get_name()}: {car.total_cost:.0f} SEK\n")
    
    # Create a motorcycle
    motorcycle = factory.create_vehicle(VehicleType.MOTORCYCLE)
    motorcycle.assemble_vehicle()
    print(f"Total cost for {motorcycle.get_name()}: {motorcycle.total_cost:.0f} SEK\n")

    # Create a bicycle
    bicycle = factory.create_vehicle(VehicleType.BICYCLE)
    bicycle.assemble_vehicle()
    print(f"Total cost for {bicycle.get_name()}: {bicycle.total_cost:.0f} SEK\n")

if __name__ == '__main__':
    main()