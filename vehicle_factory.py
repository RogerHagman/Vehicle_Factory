from __future__ import annotations
from enum import Enum
import logging
from vehicle import Vehicle
from car import Car
from motorcycle import Motorcycle
from bicycle import Bicycle

class VehicleType(Enum):
    """
    Enum to represent different types of vehicles.

    Attributes:
    - CAR: Represents a car.
    - MOTORCYCLE: Represents a motorcycle.
    - BICYCLE: Represents a bicycle.
    """
    CAR = 1
    MOTORCYCLE = 2
    BICYCLE = 3

class VehicleFactory:
    """
    A class providing a factory method to create vehicle instances
    based on provided type.
    
    This class intended use is to create instances of different 
    vehicles, keeping an encapsulated logic for the creation of 
    various vehicle types and ensuring that the client code 
    adheres to the Open/Closed Principle in the SOLID guidelines.

    Methods:
    - create_vehicle: 
    Creates a vehicle instance based on the provided vehicle type.
    """
    
    @staticmethod
    def create_vehicle(vehicle_type: VehicleType) -> Vehicle:
        """
        Factory method to create a vehicle based on the given type.
        
        This method serves as a single point for creating instances of various vehicle types, 
        enabling easy management and extension of the creation logic, and ensuring that the 
        client code remains decoupled from the specific vehicle classes.

        Args:
        - vehicle_type (VehicleType): 
        Enum representing the type of vehicle to be created.

        Returns:
        Vehicle: An instance of a subclass of Vehicle corresponding
        to the provided vehicle_type.

        Raises:
        - ValueError: 
        If the provided vehicle_type is None or not recognized.
        
        Usage:
        >>> vehicle = VehicleFactory.create_vehicle(VehicleType.CAR)
        """
        if vehicle_type is None:
            logging.error("None provided as the vehicle_type")
            raise ValueError("Vehicle type must not be None")

        if vehicle_type == VehicleType.CAR:
            return Car()
        elif vehicle_type == VehicleType.MOTORCYCLE:
            return Motorcycle()
        elif vehicle_type == VehicleType.BICYCLE:
            return Bicycle()
        else:
            logging.error(f"Vehicle type {vehicle_type} not recognized")
            raise ValueError(f"Vehicle type {vehicle_type} not recognized")