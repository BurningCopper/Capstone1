class Totals:
    """Calculate the subtotal and total after tax"""

    def __init__(self, order_lines):
        """Initialize the order price function(s)"""
        self.order_lines = order_lines
    
    def formatted(self):
        sub_total = 0
        for order_line in self.order_lines:
            sub_total = sub_total + (float(order_line[1]) * float(order_line[2]))
        print(f"Subtotal\t${sub_total:>10.2f}".format())
        print(f"Tax\t\t${(0.075 * sub_total):>10.2f}".format())
        print(f"Total\t\t${(sub_total + (0.075 * sub_total)):>10.2f}".format())
