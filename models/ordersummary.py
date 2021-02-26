class OrderSummary:
    """Format the entire order"""

    def __init__(self, order_lines):
        self.order_lines = order_lines
    
    def formatted(self):
        print("=======================================")
        print("|Part number\t|Unit Price  |Quantity|")
        print("=======================================")
        for order_line in self.order_lines:
                print(f"|{order_line[0]:>8}\t|${float(order_line[1]):>11.2f}|  {int(order_line[2]):6.0f}|".format())
                print(" _____________________________________")
        print("=======================================")