from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
import re

class VehicleType(Enum):
    CAR = 1
    MOTORCYCLE = 2
    BICYCLE = 3

class Vehicle(ABC):
    _total_cost = 0
    _no_of_tires = 0
    
    @property
    @abstractmethod
    def chassis_cost(self) -> float:
        pass
    
    def fit_chassis(self):
        self._total_cost += self.chassis_cost
    
    def fit_tires(self, no_of_tires: int):
        """Fit n tires to the vehicle."""
        self._no_of_tires = no_of_tires
        self._total_cost += self._no_of_tires * self.tire_cost
    
    def assemble_vehicle_common(self, no_of_tires: int):
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
        pass
    
    @property
    @abstractmethod
    def tire_cost(self) -> float:
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        return self.__class__.__name__
    
    @property
    def total_cost(self):
        return self._total_cost
    
    @total_cost.setter
    def total_cost(self, value):
        self._total_cost = value
    

class EnginePoweredVehicle(Vehicle, ABC):
    _engine_size = None

    @property
    def engine_cost(self):
        return self.calculate_engine_cost(self._engine_size)

    @abstractmethod
    def calculate_engine_cost(self, size_cc: int) -> float:
        pass
    
    def fit_engine(self, size_cc: int):
        engine_cost = self.calculate_engine_cost(size_cc)
        self._total_cost += engine_cost
        self._engine_size = size_cc
        print(f"{self.get_name()} engine ({size_cc}cc) cost: {engine_cost:.0f} SEK")

    def assemble_vehicle_common(self, no_of_tires: int, engine_size_cc: int):
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

class Car(EnginePoweredVehicle):
    
    def __init__(self, no_of_tires = 4):
        self._no_of_tires = no_of_tires
    
    def get_name(self) -> str:
        return super().get_name()

    @property
    def chassis_cost(self) -> float:
        return 50_000.00
    
    @property
    def engine_cost(self):
        return super().engine_cost
    
    @property
    def tire_cost(self) -> float:
        return 3000.0
    
    def calculate_engine_cost(self, size_cc: int) -> float:
        return 25_000 + (49.50 * size_cc)
    
    def assemble_vehicle(self, engine_size_cc: int):
        order = super().assemble_vehicle_common(4, engine_size_cc)
        return order


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
        return 20_000.00
    
    @property
    def tire_cost(self) -> float:
        return 2000.0
    
    def calculate_engine_cost(self, size_cc: int) -> float:
        return 15_000 + (39.50 * size_cc)
    
    def assemble_vehicle(self, engine_size_cc: int):
        return self.assemble_vehicle_common(self._no_of_tires, engine_size_cc)

class Bicycle(Vehicle):
    
    def __init__(self, no_of_tires = 2):
        self._no_of_tires = no_of_tires
    
    def get_name(self) -> str:
        return super().get_name()
    
    @property
    def chassis_cost(self) -> float:
        return 2000.00
    
    @property
    def tire_cost(self) -> float:
        return 800.0
    
    def assemble_vehicle(self, engine_size=None):
        return super().assemble_vehicle_common(self._no_of_tires)

class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type: VehicleType) -> Vehicle:
        """Factory method to create a vehicle based on the given type."""
        if vehicle_type == VehicleType.CAR:
            return Car()
        elif vehicle_type == VehicleType.MOTORCYCLE:
            return Motorcycle()
        elif vehicle_type == VehicleType.BICYCLE:
            return Bicycle()
        else:
            raise ValueError(f"Vehicle type {vehicle_type} not recognized")

class OrderManager:
    
    def __init__(self):
        self._orders = []
        self.total_cost = 0
    
    def add_order(self, order):
        self._orders.append(order)
        self.total_cost += order["TotalCost"]
        self._print_order_details(order)
        
    def print_total_cost(self):
        print(f"\nTotal cost of all orders: {self.total_cost} SEK")

    def get_total_cost(self):
        return self.total_cost
    
    def get_total_orders(self):
        return len(self._orders)
    
    def format_order(self, order, index=None):
        order_str_list = []
        if index is not None:
            order_str_list.append(f"{index}. {order['Name']}: {order['TotalCost']} SEK\n")
        else:
            order_str_list.append(f"{order['Name']}:\n")

        if order.get("Parts"):
            for part, cost in order["Parts"].items():
                order_str_list.append(f"    {part}: {cost} SEK\n")
        else:
            order_str_list.append("    No parts details available.\n")

        order_str_list.append(f"    Total: {order['TotalCost']} SEK\n")

        return ''.join(order_str_list)

    def _print_order_details(self, order):
        print(self.format_order(order))
    
    def generate_invoice(self):
        with open("invoice.txt", "w") as file:
            file.write("INVOICE\n")
            file.write("=======\n\n")
            for i, order in enumerate(self._orders, 1):
                file.write(self.format_order(order, i))
            file.write("\n")
            file.write(f"Total Cost: {self.get_total_cost()} SEK\n")

def main():

    factory = VehicleFactory()
    order_manager = OrderManager()

    app = MainApp(factory=factory, order_manager=order_manager)
    app.run()

class MainApp(App):
    def __init__(self, factory: VehicleFactory, 
                 order_manager: OrderManager, **kwargs):

        super().__init__(**kwargs)
        self.factory = factory
        self.order_manager = order_manager

    def build(self):
        self.factory = VehicleFactory()
        self.order_manager = OrderManager()
        
        self.main_layout = BoxLayout(orientation="vertical")
        
        self.dropdown = DropDown()
        for vehicle in ["Car", "Motorcycle", "Bicycle"]:
            btn = Button(text=vehicle, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)
        
        self.main_button = Button(text="Select Vehicle")
        self.main_button.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=self.on_select)
        
        self.engine_input = TextInput(hint_text="Enter Engine Size", input_filter="int")
        self.place_order_button = Button(text="Place Order")
        self.place_order_button.bind(on_press=self.place_order)
        self.total_cost_label = Label(text="Total Cost: 0")
        
        self.main_layout.add_widget(self.main_button)
        self.main_layout.add_widget(self.engine_input)
        self.main_layout.add_widget(self.place_order_button)
        self.main_layout.add_widget(self.total_cost_label)

        self.generate_invoice_button = Button(text="Generate Invoice")
        self.generate_invoice_button.bind(on_press=self.generate_invoice)
        self.main_layout.add_widget(self.generate_invoice_button)
        
        return self.main_layout
    
    def generate_invoice(self, instance):
        self.order_manager.generate_invoice()
        self.total_cost_label.text = "Invoice generated!"

    def on_select(self, instance, vehicle):
        self.main_button.text = vehicle
        self.engine_input.disabled = (vehicle == "Bicycle")
    
    def place_order(self, instance):
        vehicle_type_map = {
            "Car": VehicleType.CAR,
            "Motorcycle": VehicleType.MOTORCYCLE,
            "Bicycle": VehicleType.BICYCLE
        }
        
        # Check if a vehicle type has been selected
        if self.main_button.text not in vehicle_type_map:
            self.total_cost_label.text = "Please select a vehicle type!"
            return
        
        # Check if engine size is entered (when needed)
        if not self.engine_input.disabled and not self.engine_input.text.isdigit():
            self.total_cost_label.text = "Please enter a valid engine size!"
            return
        
        vehicle_type = vehicle_type_map.get(self.main_button.text)
        engine_size = None if self.engine_input.disabled else int(self.engine_input.text)
        
        vehicle = self.factory.create_vehicle(vehicle_type)
        order = vehicle.assemble_vehicle(engine_size)
        self.order_manager.add_order(order)
        
        # Reset inputs for the next order
        self.main_button.text = "Select Vehicle"
        self.engine_input.text = ""
        
        self.total_cost_label.text = f"Total Cost: {self.order_manager.get_total_cost()}"

# Run the application       
if __name__ == "__main__":
    main()