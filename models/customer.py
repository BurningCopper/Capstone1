class Customer:
    """Format input customer data"""

    def __init__(self, first_name, last_name, email_address):
        """Initialize the Customer function(s)"""
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address

    def formatted(self):
        print(f"{self.first_name.title()} {self.last_name.title()}")
        print(f"{self.email_address.lower()}")
        print("=======================================")
