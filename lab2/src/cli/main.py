"""Console menu demonstrating the plant domain."""

from src.models.finance import Account, Supplier
from src.models.orders import Customer, Order, OrderLine
from src.models.parts import BrakePart, EnginePart
from src.models.people import Engineer, Manager, Worker
from src.models.plant import Plant
from src.models.production import Machine, ProductionLine, ProductionOrder
from src.models.quality import QualityCheck, QualityStandard
from src.models.warehouse import StorageBin, Warehouse
from src.services.finance_service import FinanceService
from src.services.inventory_service import InventoryService
from src.services.production_service import ProductionService

def seed(plant: Plant) -> None:
    """Pre-populate the plant with demo data."""
    plant.hire(Worker("W1", "Ivan Petrov", "L1"))
    plant.hire(Engineer("E1", "Anna Sidorova", "engines"))
    plant.hire(Manager("M1", "Oleg Kuznetsov", "production"))

    plant.register_part(EnginePart("P1", "Piston", 120.0, 2.5, 150))
    plant.register_part(BrakePart("P2", "Brake Pad", 45.0, 0.8, True))

    line = ProductionLine("L1", "P1")
    line.add_machine(Machine("MCH1", "CNC-1", 100))
    line.add_machine(Machine("MCH2", "CNC-2", 80))
    plant.add_line(line)

    wh = Warehouse("WH1", "Novosibirsk")
    b = StorageBin("B1", 10_000)
    b.store("P1", 500)
    b.store("P2", 300)
    wh.add_bin(b)
    plant.add_warehouse(wh)

    plant.suppliers.register(Supplier("S1", "SteelCo", "steel"))

def menu() -> None:
    account = Account("ACC1", 100_000.0)
    plant = Plant("AutoParts LLC", account)
    seed(plant)
    production_service = ProductionService()
    inventory_service = InventoryService(next(iter(plant.warehouses.values())))
    finance_service = FinanceService(plant)

    actions = {
        "1": ("Hire worker", action_hire_worker),
        "2": ("Fire employee", action_fire_employee),
        "3": ("Show payroll", action_show_payroll),
        "4": ("Run production order", action_run_production),
        "5": ("Place customer order", action_place_order),
        "6": ("Fulfil order from warehouse", action_fulfil),
        "7": ("Charge order", action_charge),
        "8": ("Quality check", action_quality),
        "9": ("Show plant summary", action_summary),
        "0": ("Exit", None),
    }

    while True:
        print("\n=== Automotive Parts Plant ===")
        for key, (label, _) in actions.items():
            print(f"  {key}) {label}")
        choice = input("> ").strip()
        if choice == "0":
            print("Bye")
            return
        if choice not in actions:
            print("Unknown option")
            continue
        actions[choice][1](plant, production_service, inventory_service, finance_service)

def action_hire_worker(plant, *_):
    eid = input("id: ").strip()
    name = input("name: ").strip()
    line = input("line code: ").strip()
    plant.hire(Worker(eid, name, line))
    print("Hired.")

def action_fire_employee(plant, *_):
    eid = input("id: ").strip()
    try:
        plant.fire(eid)
        print("Fired.")
    except Exception as e:
        print(f"Error: {e}")
        
def action_show_payroll(plant, *_):
    print(f"Total payroll: {plant.total_payroll()}")

def action_run_production(plant, production_service, *_):
    oid = input("production order id: ").strip()
    qty = int(input("quantity: ").strip())
    line_id = input("line id: ").strip()
    if line_id not in plant.lines:
        print("No such line")
        return
    order = ProductionOrder(oid, plant.lines[line_id].part_id, qty)
    plant.add_production_order(order)
    produced = production_service.run_order(order, plant.lines[line_id])
    print(f"Produced {produced} units, done={order.is_done()}")

def action_place_order(plant, *_):
    cid = input("customer id: ").strip()
    name = input("customer name: ").strip()
    country = input("country: ").strip()
    customer = Customer(cid, name, country)
    order_id = input("order id: ").strip()
    order = Order(order_id, customer)
    while True:
        pid = input("part id (blank to finish): ").strip()
        if not pid:
            break
        qty = int(input("quantity: ").strip())
        price = float(input("unit price: ").strip())
        order.add_line(OrderLine(pid, qty, price))
    plant.place_order(order)
    print(f"Order {order_id} value={order.total_value()}")

def action_fulfil(plant, _, inventory_service, __):
    oid = input("order id: ").strip()
    order = plant.find_order(oid)
    inventory_service.fulfil(order)
    print(f"Order {oid} shipped")

def action_charge(plant, _, __, finance_service):
    oid = input("order id: ").strip()
    order = plant.find_order(oid)
    customer_account = Account(f"c-{order.customer.customer_id}", 1_000_000.0)
    finance_service.charge_order(order, customer_account)
    print(f"Charged {order.total_value()}")

def action_quality(*_):
    std = QualityStandard("Q1", 0.05)
    check = QualityCheck("C1", std)
    size = int(input("batch size: ").strip())
    defects = int(input("defects: ").strip())
    ok = check.evaluate(size, defects)
    print(f"Passed={ok}, pass rate={check.pass_rate()}")

def action_summary(plant, *_):
    print(f"Plant: {plant.name}")
    print(f"Employees: {len(plant.employees)}")
    print(f"Parts: {len(plant.parts)}")
    print(f"Lines: {len(plant.lines)}")
    print(f"Orders: {len(plant.orders)}")
    print(f"Warehouse units: {sum(w.total_units() for w in plant.warehouses.values())}")
    print(f"Revenue: {plant.total_revenue()}")

if __name__ == "__main__":
    menu()