from __future__ import annotations
from abc import ABC, abstractmethod
from vehicle import Vehicle
import logging

class EnginePoweredVehicle(Vehicle, ABC):
    """
    An abstract class representing a generic engine-powered vehicle.
    
    This class provides the base functionality and structure for
    various types of engine-powered vehicles, such as cars and 
    motorcycles, extending the generic `Vehicle` class.
    
    Attributes:
        _engine_size: 
        Engine size of the vehicle, in cubic centimeters (cc).
    """
    
    _engine_size = None

    @property
    def engine_cost(self):
        """
        Calculate and return the cost of the engine.
        
        Returns:
            float: Cost of the engine, computed based on its size.
        """
        return self.calculate_engine_cost(self._engine_size)

    @abstractmethod
    def calculate_engine_cost(self, size_cc: int) -> float:
        """
        Abstract method to calculate the engine cost based on its size.
        
        Args:
            size_cc (int): The size of the engine in cubic centimeters.
        
        Returns:
            float: The computed cost of the engine.
        
        Note:
            This method must be implemented by all subclasses.
        """
        pass
    
    def fit_engine(self, size_cc: int):
        """
        Fit an engine of a specified size to the vehicle and update the
        total cost.
        
        Args:
            size_cc (int): 
            The size of the engine to be fitted, in cubic centimeters.
        """
        engine_cost = self.calculate_engine_cost(size_cc)
        self._total_cost += engine_cost
        self._engine_size = size_cc
        logging.info(f"New engine ({size_cc}cc) fitted")

    def assemble_vehicle_common(self, no_of_tires: int,
                                engine_size_cc: int):
        """
        Assemble the vehicle, including fitting the chassis, tires,
        and engine. Finalizing by calculating the total cost.
        
        Args:
            no_of_tires (int):
            The number of tires to be fitted to the vehicle.
            engine_size_cc (int):
            The size of the engine to be fitted, in cubic centimeters.
        
        Returns:
            dict: A summary including the name of the vehicle, 
            cost of each part, and the total cost of the 
            assembled vehicle.
        """
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