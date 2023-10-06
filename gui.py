from order_manager import OrderManager
from vehicle_factory import VehicleFactory
from vehicle_factory import VehicleType
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.widget import Widget
import logging

class MainApp(App):
    def __init__(self, factory: VehicleFactory, 
                 order_manager: OrderManager, **kwargs):

        super().__init__(**kwargs)
        self.factory = factory
        self.order_manager = order_manager

    def build(self):
        self.factory = VehicleFactory()
        self.order_manager = OrderManager()
        
        # Setting the window color to black
        Window.clearcolor = (0, 0, 0, 1)
        Window.size=(400, 400)
        
        self.main_layout = BoxLayout(orientation="vertical")
        
        self.dropdown = DropDown()
        
        # Button colors
        button_colors = {
            "Car": [1, 0, 0, 1],  # Red
            "Motorcycle": [0, 1, 0, 1],  # Green
            "Bicycle": [0, 0, 1, 1]  # Blue
        }
        
        for vehicle in ["Car", "Motorcycle", "Bicycle"]:
            btn = Button(text=vehicle, size_hint_y=None, height=40, 
                        size_hint_x=0.5, 
                        background_color=button_colors[vehicle],
                        color=[1, 1, 1, 1])
            btn.bind(
                on_release=lambda btn=btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)
        
        self.main_button = Button(text="Select Vehicle to Order", 
                          size_hint_y=None, height=40, 
                          background_normal='Solid_yellow.png', 
                          background_down='Solid_yellow.png',
                          color=[0, 0, 0, 1])
        
        self.main_button.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=self.on_select)
        
        engine_input_layout = BoxLayout(size_hint_y=None, height=230)
        self.engine_input = \
            TextInput(hint_text="Size of Engine to Fit", 
                      input_filter="int", 
                      size_hint_y=None, 
                      height=40)
        
        # Fixating the Input window by adding Empty space as padding.
        engine_input_layout.add_widget(Widget(size_hint_x=0.50))
        engine_input_layout.add_widget(self.engine_input)
        engine_input_layout.add_widget(Widget(size_hint_x=0.50))

        button_layout = BoxLayout(size_hint_y=None, height=40)
        self.place_order_button = Button(text="Place Order", 
                                        size_hint_x=0.5, height=42,
                                        size_hint_y=None, 
                                        background_color=[1, 0.8, 0, 1], 
                                        color=[0, 0, 0, 1])
        # Fixating the Order button by adding Empty space as padding.       
        button_layout.add_widget(Widget(size_hint_x=0.25))
        button_layout.add_widget(self.place_order_button)
        button_layout.add_widget(Widget(size_hint_x=0.25))
                
        self.place_order_button.bind(on_press=self.place_order)
                
        self.total_cost_label = \
            Label(text="Total Cost: 0", 
                  size_hint_y=None, 
                  height=40, color=[1, 1, 1, 1])

        # Adding an Invoice Button, pressing it Tallies together
        # all orders and creates an invoice generated at 
        # application exit.
        self.generate_invoice_button = \
            Button(text="Generate Invoice", size_hint_y=None, 
                   height=44, background_color=[0, 0, 1, 1])
        self.generate_invoice_button.bind(on_press=self.generate_invoice)

        self.main_layout.add_widget(self.main_button)
        self.main_layout.add_widget(engine_input_layout)
        self.main_layout.add_widget(button_layout)
        self.main_layout.add_widget(self.total_cost_label)
        self.main_layout.add_widget(self.generate_invoice_button)
        return self.main_layout
    
    def generate_invoice(self, instance):
        self.order_manager.generate_invoice()
        self.total_cost_label.text = "Invoice Generated!"

    def on_select(self, instance, vehicle):
        self.main_button.text = vehicle
        self.engine_input.disabled = (vehicle == "Bicycle")
    
    def place_order(self, instance):
        vehicle_type_map = {
            "Car": VehicleType.CAR,
            "Motorcycle": VehicleType.MOTORCYCLE,
            "Bicycle": VehicleType.BICYCLE
        }
        vehicle_type = vehicle_type_map.get(self.main_button.text)
        
        # Check if a vehicle type has been selected
        if vehicle_type is None:
            popup = Popup(title='Input Error',
                        content=Label(text='Please select a vehicle type.'),
                        size_hint=(0.5, 0.3))
            popup.open()
            return
        
        # Displays a popup for the case where the engine 
        # size is not selected when purchasing motor vehicles.
        if not self.engine_input.disabled and \
            not self.engine_input.text.strip():

            popup = Popup(title='Input Error',
                        content=Label(text='Please enter engine size.'),
                        size_hint=(0.5, 0.3))
            popup.open()
            return
        
        engine_size = None if self.engine_input.disabled \
                            else int(self.engine_input.text)
        
        vehicle = self.factory.create_vehicle(vehicle_type)
        order = vehicle.assemble_vehicle(engine_size)
        self.order_manager.add_order(order)
        
        self.total_cost_label.text = \
            f"Total Cost: {self.order_manager.get_total_cost()}"
        
        # After placing an order, the order window 
        # resets and is ready for additional orders.
        self.engine_input.text = ""  