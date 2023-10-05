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
    def tires(self):
        pass

    @property
    @abstractmethod
    def total_cost(self):
        pass

    @total_cost.setter
    @abstractmethod
    def total_cost(self, cost: float):
        pass
    
    @abstractmethod
    def fit_tires(self):
        """Will fit an appropriate number of tires depending on the 
        vehicle type."""
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
    _no_of_tires = None
    _total_cost = 0

    def get_name(self) -> str:
        return self.__class__.__name__
    
    @property
    def tires(self):
        return self._no_of_tires
    
    @tires.setter
    def tires(self, value):
        self._no_of_tires = value
        self._total_cost += value * 3000
    
    def fit_tires(self):
        """Fit 4 tires to the car."""
        self.tires = 4
    
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
        self._total_cost += 25000 + (49.50 * size_cc)
        self.engine_size = size_cc

    def replace_engine(self, size_cc: int):
        self._total_cost += 20000 + (49.50 * size_cc)
        self.engine_size = size_cc

class Motorcycle(Vehicle, MotorVehicle):
    _engine_size = None
    _no_of_tires = None
    _total_cost = 0

    def get_name(self) -> str:
        return self.__class__.__name__
    
    @property
    def tires(self):
        return self._no_of_tires
    
    @tires.setter
    def tires(self, value):
        self._no_of_tires = value
        self._total_cost += value * 2000

    def fit_tires(self):
        """Fit 2 tires to the motorcycle."""
        self.tires = 2

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
        self._total_cost += 15000 + (39.50 * size_cc)
        self.engine_size = size_cc
    
    def replace_engine(self, size_cc: int):
        self._total_cost += 10000 + (39.50 * size_cc)
        self.engine_size = size_cc

class Bicycle(Vehicle):
    
    _total_cost = 0

    def get_name(self) -> str:
        return self.__class__.__name__
    
    @property
    def tires(self):
        return self._no_of_tires
    
    @tires.setter
    def tires(self, value):
        self._no_of_tires = value
        self._total_cost += value * 800

    def fit_tires(self):
        """Fit 2 tires to the bicycle."""
        self.tires = 2

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
    car.fit_tires()
    car.fit_engine(500)  
    print(f"{car.get_name()} cost with {car.tires} tires and a {car.engine_size}cc engine installed: {car.total_cost:.0f} SEK")

    # Create a motorcycle
    motorcycle = factory.create_vehicle(VehicleType.MOTORCYCLE)
    motorcycle.fit_tires()
    motorcycle.fit_engine(990)  # fitting a 990cc engine
    print(f"{motorcycle.get_name()} cost with {motorcycle.tires} tires and a {motorcycle.engine_size}cc engine installed: {motorcycle.total_cost:.0f} SEK")

    # Create a bicycle
    bicycle = factory.create_vehicle(VehicleType.BICYCLE)
    bicycle.fit_tires()
    print(f"{bicycle.get_name()} cost with {bicycle.tires} tires installed: {bicycle.total_cost:.0f} SEK")


if __name__ == '__main__':
    main()