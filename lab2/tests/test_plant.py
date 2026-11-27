import pytest
from src.exceptions import EmployeeNotFoundException, PartNotFoundException, OrderNotFoundException
from src.models.plant import Plant
from src.models.finance import Account
from src.models.people import Worker
from src.models.parts import EnginePart
from src.models.orders import Customer, Order, OrderLine

def test_plant_aggregation():
    p = Plant("Test", Account("A1"))
    w = Worker("W1", "A", "L1")
    p.hire(w)
    assert len(p.employees) == 1
    p.fire("W1")
    assert len(p.employees) == 0
    with pytest.raises(EmployeeNotFoundException):
        p.fire("W1")

    e = EnginePart("P1", "Piston", 10, 1, 100)
    p.register_part(e)
    assert p.find_part("P1") == e
    with pytest.raises(PartNotFoundException):
        p.find_part("P2")

    c = Customer("C1", "Name", "US")
    o = Order("O1", c)
    o.add_line(OrderLine("P1", 1, 10.0))
    p.place_order(o)
    assert p.find_order("O1") == o
    with pytest.raises(OrderNotFoundException):
        p.find_order("O2")