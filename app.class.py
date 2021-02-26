## Creating an order proccessing program with Python


from models.customer import Customer
from models.current_order import CurrentOrder
from models.totals import Totals

class Program:
    """Start of the application"""

    def main(self):
        """The main function"""
        customer = self.input_customer_details()
        current_order = self.input_current_order()
        Customer(customer)

    def input_customer_details(self):
        print("\nEnter the customer information")
        first_name = input("\tWhat is the customer's first name? ")
        last_name = input("\tWhat is the customer's last name? ")
        email_address = input("\tWhat is the customer's e-mail address? ")
        return Customer(first_name, last_name, email_address)

    def input_current_order(self):
        # prices = [34.78, 432.25, 900]
        # order_total = Totals(prices)
        # order_total.formatted()
        order_number = input("\nWhat is the order number? ")
        order_description = input("\nWhat is the order description? (limit 60 characters) ")
        return CurrentOrder(order_number, order_description)


        
    # def input_order_items(self):
    #     line_number = input("\nHow many items are included in this order? ")
    #     line_number = int(line_number)
    #     print("\nPlease enter the following information:")
    #     counter = 0
    #     while counter < line_number:
    #         counter += 1
    #         print(f"\nFor item number {counter}:")
    #         part_number = input("\tWhat is the part number? ")
    #         unit_cost = input("\tWhat is the unit cost? ")
    #         quantity = input("\tHow many units? ")
    #         order_line = [part_number, unit_cost, quantity]
    #         order_lines.append(order_line)
    #     return (order_number, order_description, )

# print(order_lines)
    
if __name__ == '__main__':
    program = Program()
    program.main()

