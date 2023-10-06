from __future__ import annotations
from abc import ABC, abstractmethod

class Vehicle(ABC):
    _total_cost = 0
    _no_of_tires = 0
    
    @property
    @abstractmethod
    def chassis_cost(self) -> float:
        pass
    
    def fit_chassis(self):
        self._total_cost += self.chassis_cost
        print(f"{self.get_name()} Chassis Fitted")
    
    def fit_tires(self, no_of_tires: int):
        """Fit n tires to the vehicle."""
        self._no_of_tires = no_of_tires
        self._total_cost += self._no_of_tires * self.tire_cost
        print(f"New tires(x {self._no_of_tires}) fitted")
    def assemble_vehicle_common(self, no_of_tires: int):
        self.fit_chassis()
        self.fit_tires(no_of_tires)
        
        parts_and_costs = {
            "Chassis": self.chassis_cost,
            "Tires": self.tire_cost * no_of_tires,
        }
        
        self.total_cost = sum(parts_and_costs.values())
        
        return {
            "Name": self.get_name(),
            "Parts": parts_and_costs,
            "TotalCost": self.total_cost  
        }
    
    @abstractmethod
    def assemble_vehicle(self):
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
    
    @total_cost.setter
    def total_cost(self, value):
        self._total_cost = value