"""Vehicle Factory"""

from __future__ import annotations
from order_manager import OrderManager
from vehicle_factory import VehicleFactory
from gui import MainApp
from engine_powered_vehicle import EnginePoweredVehicle

def main():
    """
    Entry point for the vehicle ordering application.
    
    Initializes the Vehicle Factory and Order Manager, 
    then starts the Kivy application using these for the 
    backend logic.
    """
    factory = VehicleFactory()
    order_manager = OrderManager()

    app = MainApp(factory=factory, order_manager=order_manager)
    app.run()

# Run the application       
if __name__ == "__main__":
    main()