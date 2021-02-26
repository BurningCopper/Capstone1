class CurrentOrder:
    """Format input order data"""

    def __init__(self, order_number, order_description):
        self.order_number = order_number
        self.order_description = order_description

    def formatted(self):
        """Format the order information"""
        print(f"{self.order_number}")
        print(f"{self.order_description}")
    
