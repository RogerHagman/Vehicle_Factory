from __future__ import annotations
from abc import ABC, abstractmethod
import logging

class Vehicle(ABC):
    """
    An abstract base class representing a generic vehicle.
    
    This class provides a skeleton for assembling vehicles and 
    calculating costs associated with it, enforcing certain 
    methods and properties that must be implemented by any 
    concrete subclass.

    Attributes:
    - _total_cost: The total cost incurred in assembling the vehicle.
    - _no_of_tires: The number of tires fitted to the vehicle.
    
    Methods:
    - fit_chassis: Fits the chassis and updates the total cost.
    - fit_tires: 
    Fits a specified number of tires and updates the total cost.
    - assemble_vehicle_common: 
    Assembles common parts and calculates the cost.
    - assemble_vehicle: 
    Abstract method to be implemented by subclasses for assembling the
    vehicle.
    - get_name: 
    Abstract method to be implemented by subclasses to get the name of
    the vehicle type. Calling the super() gets a default implementation
    
    Properties:
    - chassis_cost: 
    Abstract property to be implemented by subclasses to get the cost
    of the chassis.
    - tire_cost: 
    Abstract property to be implemented by subclasses to get the cost
    of a tire.
    - total_cost: 
    Property that gets and sets the _total_cost attribute.
    """
    _total_cost = 0
    _no_of_tires = 0
    
    @property
    @abstractmethod
    def chassis_cost(self) -> float:
        """
        Abstract property that should return the cost of the vehicle's
        chassis.

        This property must be implemented by subclasses to specify the
        cost associated with the chassis of a specific type of vehicle.
        """
        pass
    
    def fit_chassis(self):
        """
        Fit the chassis to the vehicle and update the total cost.

        This method should be used to perform the operation of fitting
        the chassis during the assembly of the vehicle. It adds up the
        cost of the chassis to the total cost and logs the operation.
        """
        self._total_cost += self.chassis_cost
        # Logs Fitting Chassis
        logging.info(f"{self.get_name()} Chassis Fitted")
    
    def fit_tires(self, no_of_tires: int):
        """
        Fit a specified number of tires to the vehicle and update
        total cost.
        
        Args:
        - no_of_tires (int): The number of tires to be fitted.

        This method should be used to perform the operation of fitting
        tires during the assembly of the vehicle. It adds up the cost
        of the tires to the total cost and logs the operation.
        """
        self._no_of_tires = no_of_tires
        self._total_cost += self._no_of_tires * self.tire_cost
        # Logs Fitting of Tires
        logging.info(f"New tires(x {self._no_of_tires}) fitted")

    def assemble_vehicle_common(self, no_of_tires: int):
        """
        Common assembly logic for a vehicle, fitting the chassis and 
        tires.
        
        Args:
        - no_of_tires (int): 
        The number of tires to be fitted to the vehicle.
        
        This method fits the chassis and the specified number of tires
        to the vehicle, calculates the total cost based on these 
        operations, and returns a dictionary containing the name of 
        the vehicle, a breakdown of the parts and 
        costs, as well as the total cost.
        
        Returns:
        dict: A dictionary containing:
            - "Name": The name/type of the vehicle.
            - "Parts": A breakdown of part names and associated costs.
            - "TotalCost": The total cost of the assembled parts.
        """
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
        """
        Abstract method for assembling a vehicle.
        
        This method should be implemented by subclasses to define 
        the specific logic for assembling a given type of vehicle, 
        accounting for any unique parts and/or assembly logic that 
        pertains to that particular type of vehicle.
        """
        pass
    
    @property
    @abstractmethod
    def tire_cost(self) -> float:
        """
        Abstract property that should return the cost of a single tire.
        
        This property must be implemented by all subclasses specifying 
        the cost associated with a single tire of a specific type of 
        vehicle.
        """
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        """
        Abstract method that should return the name of the vehicle 
        type.
        
        This method should be implemented by subclasses to return a 
        string containing the name/type of the vehicle, 
        which can be utilized in logging, reporting, and any use-case
        where the type name of the vehicle is required.
        
        Default implementation returns the class name.
        """
        return self.__class__.__name__
    
    @property
    def total_cost(self):
        """
        Property to get the total cost incurred in assembling the
        vehicle.
        
        Returns:
        float: 
        The total cost incurred in assembling the vehicle uptill now.
        """
        return self._total_cost
    
    @total_cost.setter
    def total_cost(self, value):
        """
        Setter for the total cost incurred in assembling of the 
        vehicle.

        Args:
        - value (float): The value to set the total cost to.
        """
        self._total_cost = value