import pytest
from src.exceptions import InsufficientStockException, CapacityExceededException
from src.models.warehouse import StorageBin, Warehouse

def test_bin_invalid_capacity():
    with pytest.raises(CapacityExceededException):
        StorageBin("B1", 0)

def test_bin_store_and_take():
    b = StorageBin("B1", 100)
    b.store("P1", 50)
    assert b.stored["P1"] == 50
    assert b.take("P1", 20) == 20
    assert b.stored["P1"] == 30
    
    with pytest.raises(InsufficientStockException):
        b.take("P1", 40)
    with pytest.raises(CapacityExceededException):
        b.store("P1", 80)

def test_warehouse():
    w = Warehouse("W1", "Address")
    b1 = StorageBin("B1", 100)
    b2 = StorageBin("B2", 100)
    b1.store("P1", 50)
    b2.store("P2", 20)
    w.add_bin(b1)
    w.add_bin(b2)
    
    assert w.total_units() == 70
    assert w.available("P1") == 50
    assert w.find_bin_with("P2") == b2
    
    with pytest.raises(InsufficientStockException):
        w.find_bin_with("P3")