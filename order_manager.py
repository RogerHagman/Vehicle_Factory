class OrderManager:
    """
    Manages and processes vehicle orders including calculating costs
    and generating invoices.

    Attributes:
        _orders (list[dict]): A list storing the details of each 
        vehicle order.
        total_cost (float): A current total cost of all orders added.
    """
    
    def __init__(self):
        """
        Initializes a new instance of OrderManager with an empty 
        orderlist and zero total cost.
        """
        self._orders = []
        self.total_cost = 0
    
    def add_order(self, order:dict):
        """
        Adds a new order to the order list, updates the total cost,
        and prints the order details.

        Args:
            order (dict): 
            A dictionary containing the details of the order, 
            expected to contain keys like "TotalCost" and "Name".
        """
        self._orders.append(order)
        self.total_cost += order["TotalCost"]
        self._print_order_details(order)
        
    def print_total_cost(self):
        """Prints the total cost of all orders in a formatted string."""
        print(f"\nTotal cost of all orders: {self.total_cost} SEK")

    def get_total_cost(self) -> float:
        """Returns the total cost of all orders."""
        return self.total_cost
    
    def get_total_orders(self) -> int:
        """Returns the total number of orders."""
        return len(self._orders)
    
    def format_order(self, order: dict, index: int = None) -> str:
        """
        Formats the order details into a readable string.

        Args:
            order (dict): 
            A dictionary containing the details of the order.
            index (int, optional): 
            The index of the order, used for numbering in the 
            output string. Default is None.

        Returns:
            str: A formatted string containing the order details.
        """
        order_str_list = []
        if index is not None:
            order_str_list.append(
                f"\n{index}. Vehicle Type: {order['Name'].upper()}\
                     \n    Parts    |    Price \n")
        else:
            order_str_list.append(f"{order['Name']}:\n")

        if order.get("Parts"):
            for part, cost in order["Parts"].items():
                order_str_list.append(f"    {part}: {cost} SEK\n")
        else:
            order_str_list.append("    No parts details available.\n")

        order_str_list.append(f"    Total: {order['TotalCost']} SEK\n")

        return ''.join(order_str_list)

    def _print_order_details(self, order: dict):
        """
        Prints the formatted details of the specified order.

        Args:
            order (dict): 
            A dictionary containing the details of the order.
        """
        print(self.format_order(order))
    
    def generate_invoice(self):
        """
        Generates an invoice detailing all orders saving it in .txt
        format.
        """
        with open("invoice.txt", "w") as file:
            file.write("           INVOICE\n")
            file.write("================================\n")
            for i, order in enumerate(self._orders, 1):
                file.write(self.format_order(order, i))
            file.write("\n")
            file.write(f"Total Cost: {self.get_total_cost()} SEK\n")