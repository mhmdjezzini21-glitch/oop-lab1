"""Customer orders."""

from src.exceptions import InvalidOrderDataException, PartNotFoundException

class Customer:
    """A customer who buys parts."""

    def __init__(self, customer_id: str, company_name: str, country: str):
        if not customer_id or not company_name:
            raise InvalidOrderDataException("id and name are required")
        self.customer_id = customer_id
        self.company_name = company_name
        self.country = country

    def __repr__(self) -> str:
        return f"Customer({self.customer_id}, {self.company_name})"

class OrderLine:
    """One line of an order: a part and quantity."""

    def __init__(self, part_id: str, quantity: int, unit_price: float):
        if quantity <= 0:
            raise InvalidOrderDataException("quantity must be positive")
        if unit_price <= 0:
            raise InvalidOrderDataException("unit price must be positive")
        self.part_id = part_id
        self.quantity = quantity
        self.unit_price = unit_price

    def total(self) -> float:
        return round(self.quantity * self.unit_price, 2)

class Order:
    """A customer order consisting of several order lines."""

    def __init__(self, order_id: str, customer: Customer):
        self.order_id = order_id
        self.customer = customer
        self.lines = []
        self.status = "new"

    def add_line(self, line: OrderLine) -> None:
        self.lines.append(line)

    def total_value(self) -> float:
        return round(sum(line.total() for line in self.lines), 2)

    def mark_shipped(self) -> None:
        if not self.lines:
            raise InvalidOrderDataException("cannot ship empty order")
        self.status = "shipped"

    def find_line(self, part_id: str) -> OrderLine:
        for line in self.lines:
            if line.part_id == part_id:
                return line
        raise PartNotFoundException(part_id)