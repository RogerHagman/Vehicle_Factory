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

    def _print_order_details(self, order):
        print(self.format_order(order))
    
    def generate_invoice(self):
        with open("invoice.txt", "w") as file:
            file.write("           INVOICE\n")
            file.write("================================\n")
            for i, order in enumerate(self._orders, 1):
                file.write(self.format_order(order, i))
            file.write("\n")
            file.write(f"Total Cost: {self.get_total_cost()} SEK\n")