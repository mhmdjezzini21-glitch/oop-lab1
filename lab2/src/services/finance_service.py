from src.models.finance import Transaction
from src.models.orders import Order
from src.models.plant import Plant

class FinanceService:
    """Charges orders and pays salaries."""

    def __init__(self, plant: Plant):
        self.plant = plant

    def charge_order(self, order: Order, customer_account) -> Transaction:
        transaction = Transaction(
            transaction_id=f"txn-{order.order_id}",
            source=customer_account,
            target=self.plant.account,
            amount=order.total_value(),
        )
        transaction.execute()
        return transaction

    def pay_salaries(self) -> float:
        total = self.plant.total_payroll()
        self.plant.account.withdraw(total)
        return total