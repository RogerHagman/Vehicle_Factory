from __future__ import annotations
from abc import ABC, abstractmethod
from vehicle import Vehicle

class EnginePoweredVehicle(Vehicle, ABC):
    _engine_size = None

    @property
    def engine_cost(self):
        return self.calculate_engine_cost(self._engine_size)

    @abstractmethod
    def calculate_engine_cost(self, size_cc: int) -> float:
        pass
    
    def fit_engine(self, size_cc: int):
        engine_cost = self.calculate_engine_cost(size_cc)
        self._total_cost += engine_cost
        self._engine_size = size_cc
        print(f"New engine ({size_cc}cc) fitted")

    def assemble_vehicle_common(self, no_of_tires: int, engine_size_cc: int):
        self.fit_chassis()
        self.fit_tires(no_of_tires)
        self.fit_engine(engine_size_cc)
        
        parts_and_costs = {
            "Chassis": self.chassis_cost,
            "Tires": self.tire_cost * no_of_tires,
            "Engine": self.calculate_engine_cost(engine_size_cc)
        }
        
        self.total_cost = sum(parts_and_costs.values())
        
        return {
            "Name": self.get_name(),
            "Parts": parts_and_costs,
            "TotalCost": self.total_cost
        }