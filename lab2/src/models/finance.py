"""Finance: accounts, transactions, suppliers."""

from src.exceptions import InsufficientFundsException, SupplierNotFoundException

class Account:
    """A bank account with a balance."""

    def __init__(self, account_id: str, balance: float = 0.0):
        self.account_id = account_id
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise InsufficientFundsException("deposit must be positive")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise InsufficientFundsException("insufficient funds")
        self.balance -= amount

class Transaction:
    """A transfer between two accounts."""

    def __init__(self, transaction_id: str, source: Account, target: Account, amount: float):
        self.transaction_id = transaction_id
        self.source = source
        self.target = target
        self.amount = amount
        self.executed = False

    def execute(self) -> None:
        self.source.withdraw(self.amount)
        self.target.deposit(self.amount)
        self.executed = True

class Supplier:
    """A supplier that delivers raw materials."""

    def __init__(self, supplier_id: str, name: str, material: str):
        self.supplier_id = supplier_id
        self.name = name
        self.material = material
        self.deliveries = 0

    def record_delivery(self, units: int) -> None:
        if units <= 0:
            raise ValueError("units must be positive")
        self.deliveries += units

class Invoice:
    """A payable or receivable invoice."""

    def __init__(self, invoice_id: str, amount: float, paid: bool = False):
        self.invoice_id = invoice_id
        self.amount = amount
        self.paid = paid

    def pay(self) -> None:
        self.paid = True

class SupplierRegistry:
    """Registry of suppliers."""

    def __init__(self):
        self.suppliers = {}

    def register(self, supplier: Supplier) -> None:
        self.suppliers[supplier.supplier_id] = supplier

    def get(self, supplier_id: str) -> Supplier:
        if supplier_id not in self.suppliers:
            raise SupplierNotFoundException(supplier_id)
        return self.suppliers[supplier_id]

    def total_deliveries(self) -> int:
        return sum(s.deliveries for s in self.suppliers.values())