from models.ordersummary import OrderSummary
from models.totals import Totals


order_lines = [
    ["12345678", "23.45", "3"],
    ["90123456", "18.95", "2"],
]

order_summary = OrderSummary(order_lines)
order_summary.formatted()

totals = Totals(order_lines)
totals.formatted()