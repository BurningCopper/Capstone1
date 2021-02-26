## Creating an order proccessing program with Python


from models.customer import Customer
from models.current_order import CurrentOrder
from models.totals import Totals
from models.ordersummary import OrderSummary


print("\nEnter the customer information")
first_name = input("\tWhat is the customer's first name? ")
last_name = input("\tWhat is the customer's last name? ")
email_address = input("\tWhat is the customer's e-mail address? ")

print("\nEnter the order information:")
order_number = input("\tWhat is the order number? ")
order_description = input("\tWhat is the order description? (limit 60 characters) ")


print("\nEnter information for the individual items:")
line_number = input("\tHow many items are included in this order? ")
line_number = int(line_number)

print("\nPlease enter the following information:")
counter = 0
order_lines = []
order_prices = []
while counter < line_number:
    counter += 1
    print(f"\nFor item number {counter}:")
    part_number = input("\tWhat is the part number? ")
    unit_cost = input("\tWhat is the unit cost? ")
    quantity = input("\tHow many units? ")
    order_line = [part_number, unit_cost, quantity]
    order_lines.append(order_line)

print("\n Invoice for the order:")

customer = Customer(first_name, last_name, email_address)
current_order = CurrentOrder(order_number, order_description)
order_summary = OrderSummary(order_lines)
totals = Totals(order_lines)

customer.formatted()
current_order.formatted()
order_summary.formatted()
totals.formatted()