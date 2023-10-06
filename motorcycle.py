from engine_powered_vehicle import EnginePoweredVehicle
import pricelist

class Motorcycle(EnginePoweredVehicle):
    
    def __init__(self, no_of_tires = 2):
        self._no_of_tires = no_of_tires

    def get_name(self) -> str:
        return super().get_name()
    
    @property
    def engine_cost(self):
        return super().engine_cost
    
    @property
    def chassis_cost(self) -> float:
        return pricelist.MOTORCYCLE_CHASSIS
    
    @property
    def tire_cost(self) -> float:
        return pricelist.MOTORCYCLE_TIRE
    
    def calculate_engine_cost(self, size_cc: int) -> float:
        return pricelist.MOTORCYCLE_ENGINE_MTRL \
            + (pricelist.MOTORCYCLE_ENGINE_FIT_COEF * size_cc)
    
    def assemble_vehicle(self, engine_size_cc: int):
        return self.assemble_vehicle_common(self._no_of_tires, engine_size_cc)