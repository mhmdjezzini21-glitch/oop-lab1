"""Top-level plant aggregate."""

from src.models.people import Employee
from src.models.parts import Part
from src.models.production import ProductionLine, ProductionOrder
from src.models.orders import Order
from src.models.warehouse import Warehouse
from src.models.finance import Account, SupplierRegistry
from src.exceptions import EmployeeNotFoundException, PartNotFoundException, OrderNotFoundException

class Plant:
    """Aggregate root combining all the plant's data."""

    def __init__(self, name: str, account: Account):
        self.name = name
        self.account = account
        self.employees = {}
        self.parts = {}
        self.lines = {}
        self.production_orders = {}
        self.orders = {}
        self.warehouses = {}
        self.suppliers = SupplierRegistry()

    def hire(self, employee: Employee) -> None:
        self.employees[employee.employee_id] = employee

    def fire(self, employee_id: str) -> None:
        if employee_id not in self.employees:
            raise EmployeeNotFoundException(employee_id)
        del self.employees[employee_id]

    def register_part(self, part: Part) -> None:
        self.parts[part.part_id] = part

    def find_part(self, part_id: str) -> Part:
        if part_id not in self.parts:
            raise PartNotFoundException(part_id)
        return self.parts[part_id]

    def add_line(self, line: ProductionLine) -> None:
        self.lines[line.line_id] = line

    def add_production_order(self, production_order: ProductionOrder) -> None:
        self.production_orders[production_order.order_id] = production_order

    def place_order(self, order: Order) -> None:
        self.orders[order.order_id] = order

    def find_order(self, order_id: str) -> Order:
        if order_id not in self.orders:
            raise OrderNotFoundException(order_id)
        return self.orders[order_id]

    def add_warehouse(self, warehouse: Warehouse) -> None:
        self.warehouses[warehouse.warehouse_id] = warehouse

    def total_payroll(self) -> float:
        return round(sum(e.compute_salary() for e in self.employees.values()), 2)

    def total_revenue(self) -> float:
        return round(sum(o.total_value() for o in self.orders.values() if o.status == "shipped"), 2)