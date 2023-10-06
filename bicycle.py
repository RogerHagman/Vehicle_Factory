from vehicle import Vehicle
import pricelist

class Bicycle(Vehicle):
    
    def __init__(self, no_of_tires = 2):
        self._no_of_tires = no_of_tires
    
    def get_name(self) -> str:
        return super().get_name()
    
    @property
    def chassis_cost(self) -> float:
        return pricelist.BICYCLE_CHASSIS
    
    @property
    def tire_cost(self) -> float:
        return pricelist.BICYCLE_TIRE
    
    def assemble_vehicle(self, engine_size=None):
        return super().assemble_vehicle_common(self._no_of_tires)