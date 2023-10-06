from engine_powered_vehicle import EnginePoweredVehicle
import pricelist

class Car(EnginePoweredVehicle):
    """
    Class Representing a Car: a subtype of EnginePoweredVehicle 
    which is in turn derived from the Vehicle Class.

    A Car is a specific type of vehicle that includes its own
    set of attributes and methods related to cost and assembly.

    Attributes:
        no_of_tires (int): Number of tires on the car.

    Properties:
        chassis_cost (float): Cost of the car's chassis.
        engine_cost (float): Cost of the car's engine.
        tire_cost (float): Cost per tire for the car.
    """

    def __init__(self, no_of_tires=4):
        """
        Initializes a Car object with a specified number of tires.

        Args:
            no_of_tires (int, optional): 
            Number of tires on the car. Defaults to 4.
        """
        self._no_of_tires = no_of_tires

    def get_name(self) -> str:
        """
        Gets the name of the vehicle.

        Overrides method in superclass to return the name specifically
        for a Car.

        Returns:
            str: Name of the vehicle.
        """
        return super().get_name()

    @property
    def chassis_cost(self) -> float:
        """
        Gets the cost of the car's chassis.

        Returns:
            float: Cost of the chassis.
        """
        return pricelist.CAR_CHASSIS

    @property
    def engine_cost(self):
        """
        Gets the cost of the car's engine.

        Returns:
            float: Cost of the engine.
        """
        return super().engine_cost

    @property
    def tire_cost(self) -> float:
        """
        Gets the cost per tire for the car.

        Returns:
            float: Cost per tire.
        """
        return pricelist.CAR_TIRE

    def calculate_engine_cost(self, size_cc: int) -> float:
        """
        Calculates the cost of the car engine based on its size.

        Args:
            size_cc (int): The size of the engine in cubic centimeters.

        Returns:
            float: Calculated engine cost.
        """
        return pricelist.CAR_ENGINE_MTRL \
            + (pricelist.CAR_ENGINE_FIT_COEF * size_cc)

    def assemble_vehicle(self, engine_size_cc: int):
        """
        Computes and returns the cost to assemble the car.

        Utilizes a common assembly method provided by the superclass
        and adds specific logic for engine size cost computation.

        Args:
            engine_size_cc (int): 
            Size of the engine in cubic centimeters.

        Returns:
            float: The total cost to assemble the car.
        """
        order = super().assemble_vehicle_common(4, engine_size_cc)
        return order