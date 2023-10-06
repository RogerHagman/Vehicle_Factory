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

logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class MainApp(App):
    """Main Application Class
    
    MainApp serves as the controller for the graphical interface of the
    vehicle ordering system. It manages the inputs from the user and 
    employs the `VehicleFactory` and `OrderManager` classes 
    to process orders and managing diffrent states.
    
    Attributes:
        factory (VehicleFactory): 
        A factory object to create vehicle instances.
        order_manager (OrderManager): 
        A manager object to handle orders.
    """
    def __init__(self, factory: VehicleFactory, 
                 order_manager: OrderManager, **kwargs):
        """
        Initializes MainApp with a vehicle factory and an order manager.
        
        Args:
            factory (VehicleFactory): 
            A factory object to create vehicle instances.
            order_manager (OrderManager): 
            A manager object to handle orders.
        """
        super().__init__(**kwargs)
        self.factory = factory
        self.order_manager = order_manager

    def build(self):
        """
        Build and initialize the UI elements for the app.
        
        Returns:
            BoxLayout: 
            A Kivy widget Using the Boxlayout sheme for UI elements.
        """
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
        """
        Employs the order manager to generate an invoice.
        
        Args:
            instance (kivy.uix.widget.Widget): 
            The widget instance that triggered the method.
        """
        self.order_manager.generate_invoice()
        self.total_cost_label.text = "Invoice Generated!"
        # Logs The Invoice generation
        logging.info("Invoice Generated!")

    def on_select(self, instance, vehicle:str):
        """
        This is an event handler for selecting vehicle types 
        from a dropdown menu.
        
        Updates the main button text and potentially disables 
        the engine input based on the vehicle type(i.e Bicycle).
        
        Args:
            instance (kivy.uix.widget.Widget): 
            The widget instance that triggered the method.
            vehicle (str): The selected vehicle type as a string.
        """
        self.main_button.text = vehicle
        self.engine_input.disabled = (vehicle == "Bicycle")
    
    def place_order(self, instance):
        """
        Place an order for a vehicle of a specified type and where it
        applies, engine size.
        
        Logs relevant events and errors during the order placement and 
        updates the UI.
        
        Args:
            instance (kivy.uix.widget.Widget): 
            The widget instance that triggered the method.
        """
        # Loggin the start of order placement
        logging.info('Attempting to place order...')  

        vehicle_type_map = {
            "Car": VehicleType.CAR,
            "Motorcycle": VehicleType.MOTORCYCLE,
            "Bicycle": VehicleType.BICYCLE
        }
        vehicle_type = vehicle_type_map.get(self.main_button.text)

        # Check if a vehicle type has been selected
        if vehicle_type is None:
            # Logs if the user fails to select a vehicle type(None)
            logging.warning('Vehicle type not selected.')
            self.show_popup('Input Error', 'Please select a vehicle type.')
            return

        # Displays a popup for the case where the engine 
        # size is not selected when purchasing motor vehicles.
        if not self.engine_input.disabled and not self.engine_input.text.strip():
            # Logs if an engine size has not been selected at all
            logging.warning('Engine size not provided for motor vehicle.')
            self.show_popup('Input Error', 'Please enter engine size.')
            return
        
        engine_size = None if self.engine_input.disabled else int(self.engine_input.text)
        
        if engine_size is not None and (engine_size <= 50 or engine_size > 8000):
            # Logs invalid engine size inputs
            logging.warning('Invalid engine size selected: %s', engine_size)
            self.show_popup('Input Error', 
                            'An engine of that size cannot be fitted!\
                            \nLegal sizes: [50cc - 8000cc]')
            return

        try:
            # Create a vehicle and assemble it with the given engine size, 
            # then add the order to the order manager and update total cost.
            vehicle = self.factory.create_vehicle(vehicle_type)
            order = vehicle.assemble_vehicle(engine_size)
            self.order_manager.add_order(order)

            self.total_cost_label.text = \
                f"Total Cost: {self.order_manager.get_total_cost()}"

            # After placing an order, the order window 
            # resets and is ready for additional orders.
            self.engine_input.text = ""
            
            # Logging of successful order placement
            logging.info('Order placed successfully.')  

        except Exception as error:
            # Logs the exception details 
            # Also interacts with the uses via Pop-Up message.
            logging.error('Error occurred while placing order: %s', str(error))
            self.show_popup(
                'Error', 
                'An error occurred while placing the order. Please try again.')

    def show_popup(self, title: str, message: str):
        """
        Display a popup window with a specified title and message.
        
        Args:
            title (str): The title of the popup window.
            message (str): The message to display in the popup window.
        """
        message_label = Label(text=message, halign='left', valign='top')
        
        message_label.text_size = (300, None)
        message_label.size_hint_y = 0.7
        
        popup = Popup(title=title,
                    content=message_label,
                    size_hint=(1, 0.5))
        popup.open()