from engine_powered_vehicle import EnginePoweredVehicle
import pricelist

class Car(EnginePoweredVehicle):
    
    def __init__(self, no_of_tires = 4):
        self._no_of_tires = no_of_tires
    
    def get_name(self) -> str:
        return super().get_name()

    @property
    def chassis_cost(self) -> float:
        return pricelist.CAR_CHASSIS
    
    @property
    def engine_cost(self):
        return super().engine_cost
    
    @property
    def tire_cost(self) -> float:
        return pricelist.CAR_TIRE
    
    def calculate_engine_cost(self, size_cc: int) -> float:
        return pricelist.CAR_ENGINE_MTRL \
            + (pricelist.CAR_ENGINE_FIT_COEF * size_cc)
    
    def assemble_vehicle(self, engine_size_cc: int):
        order = super().assemble_vehicle_common(4, engine_size_cc)
        return order