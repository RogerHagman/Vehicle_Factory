from __future__ import annotations
from enum import Enum
import logging
from vehicle import Vehicle
from car import Car
from motorcycle import Motorcycle
from bicycle import Bicycle

class VehicleType(Enum):
    CAR = 1
    MOTORCYCLE = 2
    BICYCLE = 3

class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type: VehicleType) -> Vehicle:
        """Factory method to create a vehicle based on the given type."""
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