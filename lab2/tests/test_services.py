import pytest
from src.exceptions import MachineFailureException, InsufficientStockException, InsufficientFundsException
from src.models.plant import Plant
from src.models.finance import Account
from src.models.production import Machine, ProductionLine, ProductionOrder
from src.models.warehouse import StorageBin, Warehouse
from src.models.orders import Customer, Order, OrderLine
from src.services.production_service import ProductionService
from src.services.inventory_service import InventoryService
from src.services.finance_service import FinanceService

def test_production_service():
    m = Machine("M1", "CNC", 100)
    m.break_down()
    line = ProductionLine("L1", "P1")
    line.add_machine(m)
    order = ProductionOrder("O1", "P1", 50)
    svc = ProductionService()
    with pytest.raises(MachineFailureException):
        svc.run_order(order, line)
        
    m.repair()
    svc.run_order(order, line)
    assert order.completed_units == 50

def test_inventory_service():
    w = Warehouse("W1", "Addr")
    b = StorageBin("B1", 100)
    b.store("P1", 10)
    w.add_bin(b)
    svc = InventoryService(w)
    
    c = Customer("C1", "Name", "US")
    o = Order("O1", c)
    o.add_line(OrderLine("P1", 5, 10))
    svc.fulfil(o)
    assert o.status == "shipped"
    assert w.available("P1") == 5
    
    o2 = Order("O2", c)
    o2.add_line(OrderLine("P1", 20, 10))
    with pytest.raises(InsufficientStockException):
        svc.fulfil(o2)

def test_finance_service():
    p = Plant("Test", Account("A1", 1000))
    
    # We use a fake worker here to avoid the import error!
    class FakeWorker:
        def __init__(self, id, name, line):
            self.employee_id = id
            self.hours_worked = 0
        def log_hours(self, h):
            self.hours_worked += h
        def compute_salary(self):
            return 100.0
            
    p.hire(FakeWorker("W1", "A", "L1"))
    p.employees["W1"].log_hours(100) 
    
    svc = FinanceService(p)
    
    # Plant has 1000, salary is 100, so this works
    svc.pay_salaries()
    assert p.account.balance == 900.0
    
    # Try charging an order
    c = Customer("C1", "Name", "US")
    o = Order("O1", c)
    o.add_line(OrderLine("P1", 1, 100))
    cust_acc = Account("Cust", 200)
    svc.charge_order(o, cust_acc)
    assert cust_acc.balance == 100
    assert p.account.balance == 1000.0