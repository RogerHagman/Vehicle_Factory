from engine_powered_vehicle import EnginePoweredVehicle
import pricelist


class Motorcycle(EnginePoweredVehicle):
    """
    Represents a Motorcycle, a type of Engine Powered Vehicle.

    Attributes:
        no_of_tires (int): Number of tires on the motorcycle.
    """

    def __init__(self, no_of_tires=2):
        """
        Initializes a new instance of the Motorcycle class.

        Args:
            no_of_tires (int): 
            Number of tires for the motorcycle. Default is 2.
        """
        self._no_of_tires = no_of_tires

    def get_name(self) -> str:
        """
        Retrieves the name of the motorcycle. 

        Returns:
            str: The name of the motorcycle.
        """
        return super().get_name()
    
    @property
    def engine_cost(self):
        """
        Retrieves the cost of the engine.

        Returns:
            [Type]: Cost of the engine.
        """
        return super().engine_cost
    
    @property
    def chassis_cost(self) -> float:
        """
        Retrieves the cost of the motorcycle's chassis.

        Returns:
            float: Cost of the motorcycle chassis.
        """
        return pricelist.MOTORCYCLE_CHASSIS
    
    @property
    def tire_cost(self) -> float:
        """
        Retrieves the cost of a single motorcycle tire.

        Returns:
            float: Cost of a motorcycle tire.
        """
        return pricelist.MOTORCYCLE_TIRE
    
    def calculate_engine_cost(self, size_cc: int) -> float:
        """
        Calculates the cost to manufacture and fit an engine of the
        given size.

        Args:
            size_cc (int): 
            The size of the engine in cubic centimeters (cc).

        Returns:
            float: The total cost to manufacture and fit the engine.
        """
        return pricelist.MOTORCYCLE_ENGINE_MTRL \
            + (pricelist.MOTORCYCLE_ENGINE_FIT_COEF * size_cc)
    
    def assemble_vehicle(self, engine_size_cc: int):
        """
        Assembles the motorcycle with a specified engine size.

        Args:
            engine_size_cc (int): 
            The size of the engine in cubic centimeters (cc).

        Returns:
            [Type]: Instance/details of the assembled vehicle. 
            (Return type and details depend on what the
            `assemble_vehicle_common` method returns.)
        """
        return self.assemble_vehicle_common(self._no_of_tires, engine_size_cc)