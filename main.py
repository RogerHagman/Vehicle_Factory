from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum

class VehicleType(Enum):
    CAR = 1
    MOTORCYCLE = 2
    BICYCLE = 3

class Vehicle(ABC):
    @abstractmethod
    def get_name(self) -> str:
        """Returns the name of the vehicle."""
        pass
    
    @property
    @abstractmethod
    def total_cost(self):
        pass

    @total_cost.setter
    @abstractmethod
    def total_cost(self, cost: float):
        pass
    
class MotorVehicle(ABC):
    
    @property
    @abstractmethod
    def engine_size(self):
        pass
    
    @engine_size.setter
    @abstractmethod
    def engine_size(self, size_cc: int):
        pass
    
    @property
    def engine_fitted(self) -> bool:
        return self.engine_size is not None

    @abstractmethod
    def fit_engine(self, size_cc: int):
        pass
    
    @abstractmethod
    def replace_engine(self, size_cc: int):
        pass

class Car(Vehicle, MotorVehicle):
    _engine_size = None
    _total_cost = 0

    def get_name(self) -> str:
        return self.__class__.__name__
    
    @property
    def total_cost(self):
        return self._total_cost
    
    @total_cost.setter
    def total_cost(self, cost: float):
        self._total_cost += cost

    @property
    def engine_size(self):
        return self._engine_size

    @engine_size.setter
    def engine_size(self, size_cc: int):
        self._engine_size = size_cc

    def fit_engine(self, size_cc: int):
        self._total_cost += 10000 + (6.50 * size_cc)
        self.engine_size = size_cc

    def replace_engine(self, size_cc: int):
        self._total_cost += 8000 + (6.50 * size_cc)
        self.engine_size = size_cc

class Motorcycle(Vehicle):
    _total_cost = 0

    def get_name(self) -> str:
        return self.__class__.__name__

    @property
    def total_cost(self):
        return self._total_cost
    
    @total_cost.setter
    def total_cost(self, cost: float):
        self._total_cost += cost

class Bicycle(Vehicle):
    
    _total_cost = 0

    def get_name(self) -> str:
        return self.__class__.__name__

    @property
    def total_cost(self):
        return self._total_cost
    
    @total_cost.setter
    def total_cost(self, cost: float):
        self._total_cost += cost
    
    

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
    print(car.get_name())
    car.fit_engine(200)
    car.replace_engine(300)
    print(car.total_cost)

    # Create a motorcycle
    motorcycle = factory.create_vehicle(VehicleType.MOTORCYCLE)
    print(motorcycle.get_name())

    # Create a bicycle
    bicycle = factory.create_vehicle(VehicleType.BICYCLE)
    print(bicycle.get_name())

if __name__ == '__main__':
    main()