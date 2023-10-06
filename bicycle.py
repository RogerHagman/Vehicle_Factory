from vehicle import Vehicle
import pricelist

class Bicycle(Vehicle):
    """
    A Class to represent a Bicycle: a subtype of Vehicle.
    
    A Bicycle is a specific type of vehicle that includes its own
    set of attributes and methods related to cost and assembly.
    
    Attributes:
        no_of_tires (int): Number of tires to be fitted on the bicycle.
        
    Properties:
        chassis_cost (float): Cost of the bicycle's chassis.
        tire_cost (float): Cost per tire for the bicycle.
    """
    
    def __init__(self, no_of_tires=2):
        """
        Args:
            no_of_tires (int, optional): 
            Number of tires in the bicycle. Defaults to 2.
        """
        self._no_of_tires = no_of_tires
    
    def get_name(self) -> str:
        """
        Gets the name of the vehicle.

        Returns:
            str: Name of the vehicle.
        """
        return super().get_name()
    
    @property
    def chassis_cost(self) -> float:
        """
        Gets the cost of the bicycle's chassis.

        Returns:
            float: Cost of the chassis.
        """
        return pricelist.BICYCLE_CHASSIS
    
    @property
    def tire_cost(self) -> float:
        """
        Gets the cost per tire for the bicycle.

        Returns:
            float: Cost per tire.
        """
        return pricelist.BICYCLE_TIRE
    
    def assemble_vehicle(self, engine_size=None):
        """
        Computes and returns the cost to assemble the bicycle. 
        Utilizes a common assembly method provided by the superclass.

        Args:
            engine_size (None): 
            Unused parameter for bicycles, since they have no engine. 
            Passed with None value for ease of execution purposes.
            
        Returns:
            float: The total cost to assemble the bicycle.
        """
        return super().assemble_vehicle_common(self._no_of_tires)