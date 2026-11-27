import pytest
from src.exceptions import InvalidOrderDataException, PartNotFoundException
from src.models.orders import Customer, Order, OrderLine

def test_customer_invalid():
    with pytest.raises(InvalidOrderDataException):
        Customer("", "Name", "Country")

def test_order_line_invalid():
    with pytest.raises(InvalidOrderDataException):
        OrderLine("P1", 0, 10)
    with pytest.raises(InvalidOrderDataException):
        OrderLine("P1", 1, -5)

def test_order_lifecycle():
    c = Customer("C1", "Buyer", "US")
    o = Order("O1", c)
    o.add_line(OrderLine("P1", 2, 10.0))
    o.add_line(OrderLine("P2", 1, 5.5))
    assert o.total_value() == 25.5
    
    line = o.find_line("P1")
    assert line.quantity == 2
    with pytest.raises(PartNotFoundException):
        o.find_line("P3")
        
    o.mark_shipped()
    assert o.status == "shipped"

def test_empty_order_ship():
    c = Customer("C1", "Buyer", "US")
    o = Order("O1", c)
    with pytest.raises(InvalidOrderDataException):
        o.mark_shipped()